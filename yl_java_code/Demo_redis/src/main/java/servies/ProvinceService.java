package main.java.servies;

import com.fasterxml.jackson.core.JsonProcessingException;
import main.java.domain.Province;

import java.util.List;

public interface ProvinceService {
    public List<Province> findAll();
    public String findAllJson();
}

