package com.yang.fastdfs.controller;

import com.yang.fastdfs.model.FileSystem;
import org.csource.common.NameValuePair;
import org.csource.fastdfs.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.UUID;

@RestController
@RequestMapping("/filesystem")
public class fileSystemController {

    @Value("${fastdfs.upload_location}")
    private String uploadLocation;

    // 上传文件
    @PostMapping("/upload")
    @ResponseBody
    public FileSystem upload(@RequestParam("file") MultipartFile file) throws IOException {
        FileSystem fileSystem = new FileSystem();

        // 先把文件存到本地服务器，然后通过 fastDfs的 client 上传到fastDfs服务器
        // 获取原始名称
        String originalFilename = file.getOriginalFilename();
        // 获取扩展名
        String extention = originalFilename.substring(originalFilename.lastIndexOf('.'));
        // 赋予一个随机名称
        String newFileName = UUID.randomUUID() + extention;
        File file1 = new File(uploadLocation + newFileName);
        // 上传的文件写道指定的文件内
        file.transferTo(file1);
        String newFilePath = file1.getAbsolutePath();


        try {
            ClientGlobal.initByProperties("config/fastdfs-client.properties");
            TrackerClient tracker = new TrackerClient();
            TrackerServer trackerServer = tracker.getConnection();
            StorageServer storageServer = null;
            StorageClient1 client = new StorageClient1(trackerServer, storageServer);
            // 文件原始信息
            NameValuePair[] metaList = new NameValuePair[1];
            metaList[0] = new NameValuePair("fileName", originalFilename);
            String fileId = client.upload_file1(newFilePath, null, metaList);

            fileSystem.setFileId(fileId);
            fileSystem.setFilePath(fileId);
            fileSystem.setFileName(originalFilename);
            fileSystem.setFileType(extention);

            // 文件路径存储到数据库
            // 。。。

            trackerServer.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return fileSystem;
    }

}
