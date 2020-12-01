// 所有资源加载完毕之后执行  不然有的元素还没加载出来获取不到属性
window.onload = function () {
  let oUlElement = document.querySelector('.oUl');
  let imgElements = [...oUlElement.querySelectorAll('img')];
  let btnElements = [...document.querySelectorAll('.btn')];
  let progress2Element = document.querySelector('.progress2');
  let stopBtn = document.querySelector('#stop_btn');

  // 初始化的每一张手机图片的位置，0-1之间的值，0 为最低位，1 为最高位
  let initRatio = [1, 0.4, 0, 0.4, 0.6, 0.4, 0];
  // 最低音的时候，图片 translateY 的值
  let bassVal = oUlElement.clientHeight * 0.8;
  // 随机颜色数组
  let colors = ['#ff5f5b', '#ffb66e', '#ffd96d', '#e8f898', '#8cf6f3', '#92aef0', '#b897e4'];
  let color = '';
  // 音乐列表
  let musicList = [
    './resource/mo.mp3',
    './resource/Rihanna - Only Girl (In The World).mp3',
    './resource/Remix.mp3',
    './resource/Neptune Illusion Dennis Kuo .mp3',
  ];
  let audio = null;
  let audioContext = null;
  let sourceNode = null;
  let analyser = null;
  let currentBtn = null; // 跳动的按钮

  // 给每一张图片添加一个属性 表示图片的中心点 x 坐标
  imgElements.forEach((img, index) => {
    let { x } = img.getBoundingClientRect();
    img._centerPointer = {
      x: x + img.width / 2,
    };
    // mTween 初始化一下 一些css3属性
    setTransform(img, 'translateY', getTranslateYByRatio(initRatio[index]));
  });
  btnElements.forEach((btn) => {
    setTransform(btn, 'scale', 1);
  });

  animatePhone(initRatio);

  // 鼠标移动的时候 检测鼠标的位置生成比例数组并更新视图
  oUlElement.onmousemove = function ({ clientX }) {
    let moveRatio = imgElements.map((img, index) => {
      return 1 - Math.abs(clientX - img._centerPointer.x) / window.innerWidth;
    });
    // console.log(moveRatio);
    animatePhone(moveRatio);
  };

  // 鼠标移出的时候复原
  oUlElement.onmouseleave = function () {
    animatePhone(initRatio);
  };

  // 按钮点击事件
  btnElements.forEach((btn, index) => {
    btn.onclick = function () {
      // 跳动的按钮
      currentBtn && mTween.stop(currentBtn);
      currentBtn = this;
      // 随机颜色
      color = colors[Math.floor(Math.random() * colors.length)];
      btnElements.forEach((btn) => (btn.style = ''));
      btn.style.backgroundColor = color;
      btn.style.color = 'white';
      // 播放音乐
      if (audio) {
        audio.pause();
        audio = null;
      }
      audio = new Audio();
      audio.addEventListener('canplay', play);
      audio.src = musicList[index];
      audio.volume = 1;
      console.log(audio);
    };
  });

  stopBtn.onclick = function () {
    audio && audio.pause();
  };

  function play() {
    audio.play();
    // 创建一个用来处理音频的工作环境（上下文），我们可以通过它来进行音频读取、解码等，进行一些更底层的音频操作
    audioContext = new AudioContext();
    // 设置音频数据源
    sourceNode = audioContext.createMediaElementSource(audio);
    // 获取音频时间和频率数据，以及实现数据可视化，connect 之前调用
    analyser = audioContext.createAnalyser();
    // connect 连接器，把声音数据连接到分析器，除了 createAnalyser，还有：BiquadFilterNode[提高音色]、ChannelSplitterNode[分割左右声道] 等对音频数据进行处理，然后通过 connect 把处理后的数据连接到扬声器进行播放
    sourceNode.connect(analyser);
    // connect 连接器，把声音数据连接到扬声器
    analyser.connect(audioContext.destination);
    // 得到的二进制音频数据，并解析
    parse();
  }

  function parse() {
    // console.log(analyser.frequencyBinCount);
    // analyser.frequencyBinCount : 二进制音频频率数据的数量（个数）
    // Uint8Array : 生成一个长度为 analyser.frequencyBinCount 的，用于处理二进制数据的数组
    let freqArray = new Uint8Array(analyser.frequencyBinCount);
    // console.log(freqArray);
    // 将当前频率数据复制到 freqArray 中
    analyser.getByteFrequencyData(freqArray);
    // console.log(freqArray);
    let arr = [];
    // 频谱反应的是声音各频率（frequencyBinCount）上能量的分布
    // 设置step，进行取样
    var step = Math.round(freqArray.length / 7);
    for (let i = 0; i < 7; i++) {
      arr.push(freqArray[i * step] / bassVal);
    }
    // console.log(arr);
    // 根据分析后的频谱数据生成动画
    animatePhone(arr);
    // 从 arr 样本中计算平均值
    let averageVal = arr.reduce((p, c) => p + c, 0) / arr.length + 0.5;
    animateBtn(averageVal);
    // 进度条
    animateProcess();
    if (!audio.paused) {
      requestAnimationFrame(parse);
    }
  }

  function animateBtn(scale) {
    mTween.stop(currentBtn);
    mTween({
      el: currentBtn,
      duration: 200,
      attr: {
        scale,
      },
    });
  }

  function animateProcess() {
    if (audio) {
      progress2Element.style.background = color;
      progress2Element.style.width = (audio.currentTime / audio.duration) * 100 + '%';
    }
  }

  // 根据传入的比例数组渲染 图片的高度
  function animatePhone(ratio) {
    imgElements.forEach((img, index) => {
      // img.style.transform = `translateY(${getTranslateYByRatio(ratio[index])}px)`;
      mTween.stop(img);
      mTween({
        el: img,
        duration: 200,
        attr: {
          translateY: getTranslateYByRatio(ratio[index]),
        },
      });
    });
  }

  // 根据比例获得高度
  function getTranslateYByRatio(ratio) {
    return (1 - ratio) * bassVal;
  }
};
