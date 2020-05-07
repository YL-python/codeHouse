// 粘性导航
const headerEL = document.querySelector("header");
const scrollToTop = document.querySelector(".scrollToTop")
window.addEventListener("scroll", () => {
  let height = headerEL.getBoundingClientRect().height;
  if (window.pageYOffset - height > 800) {
    if (!headerEL.classList.contains("sticky")) {
      headerEL.classList.add("sticky");
    }
  } else {
    headerEL.classList.remove("sticky")
  }
  // 返回顶部
  if (window.pageYOffset > 800) {
    scrollToTop.style.display = "block"
  } else {
    scrollToTop.style.display = "none"
  }
})

// 轮播图 js 初始化代码
const glide = new Glide('.glide', {
  type: 'carousel',
  autoplay: '18000'
})

// 轮播图标题动画显示
const captionsEL = document.querySelectorAll(".slide-caption");

// 监听事件，出来的时候加动画
glide.on(["mount.after", "run.after"], () => {
  const caption = captionsEL[glide.index];
  anime({
    targets: caption.children,
    opacity: [0, 1],
    duration: 400,
    easing: 'spring(1, 80, 10, 0)',
    delay: anime.stagger(400, {
      start: 300
    }),
    translateY: [anime.stagger([40, 10]), 0]
  });
});

// 结束的时候吧透明度还原。这样每次就都会有动画
glide.on("run.before", () => {
  document.querySelectorAll(".slide-caption > *").forEach(el => {
    el.style.opacity = 0;
  });
});

glide.mount()

// 分类js
const isotope = new Isotope(".cases", {
  layoutMode: "fitRows",
  itemSelector: ".case-item"
})

const filterBtns = document.querySelector(".filter-btns");
filterBtns.addEventListener("click", e => {
  let {
    target
  } = e;
  const filterOption = target.getAttribute("data-filter");
  if (filterOption) {
    document
      .querySelectorAll(".filter-btn.active")
      .forEach(btn => btn.classList.remove("active"));
    target.classList.add("active");
    isotope.arrange({
      filter: filterOption
    });
  }
})

// 滑动出现动画
const staggeringOption = {
  delay: 300,
  distance: "50px",
  duration: 500,
  easing: "ease-in-out",
  origin: "bottom"
};
ScrollReveal().reveal(".feature", {
  ...staggeringOption,
  interval: 350
})
ScrollReveal().reveal(".service-item", {
  ...staggeringOption,
  interval: 350
})

// 数据区域动画
const dataSectionEl = document.querySelector(".data-section");
ScrollReveal().reveal(".data-section", {
  beforeReveal: () => {
    anime({
      targets: ".data-price .num",
      innerHTML: el => {
        return [0, el.innerHTML];
      },
      duration: 2000,
      round: 1,
      easing: "easeInExpo"
    });
    dataSectionEl.style.backgroundPosition =
      `center calc(50% - ${dataSectionEl.getBoundingClientRect().bottom / 5}px)`;
  }
});

// 数据区域背景变化
window.addEventListener("scroll", () => {
  const bottom = dataSectionEl.getBoundingClientRect().bottom;
  const top = dataSectionEl.getBoundingClientRect().top;
  if (bottom > 0 && top < window.innerHeight) {
    dataSectionEl.style.backgroundPosition = `center calc(50% - ${bottom / 5}px)`;
  }
});

// 平滑滚动
const scroll = new SmoothScroll('nav a[href*="#"],.scrollToTop a[href*="#"]', {
  header: "header",
  offset: 80
});

// 探索更多按钮
const exploreBtnEls = document.querySelectorAll(".explore-btn");
exploreBtnEls.forEach(exploreBtnEl => {
  exploreBtnEl.addEventListener("click", () => {
    scroll.animateScroll(document.querySelector("#about-us"))
  })
})

//折叠按钮
const burgerEl = document.querySelector(".burger")
burgerEl.addEventListener("click", () => {
  headerEL.classList.toggle("open")
})

// 滚动的时候 折叠菜单如果打开就关闭
document.addEventListener('scrollStart',()=>{
  if(headerEL.classList.contains('open')){
    headerEL.classList.remove("open")
  }
})


/*
document.documentElement.style.setProperty('--primary-color','#ffffff')
通过 js 修改css自定义的属性
*/