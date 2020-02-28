package code_File.过滤器.路径过滤器;

import java.io.File;
import java.io.FileFilter;

public class FileFilterImpl implements FileFilter {
    @Override
    public boolean accept(File pathname) {
        return pathname.getName().toLowerCase().endsWith(".java");
    }
}
