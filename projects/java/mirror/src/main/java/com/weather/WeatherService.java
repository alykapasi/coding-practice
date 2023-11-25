package com.weather;

// import org.springframework.web.client.RestTemplate;


public class WeatherService {
    private final String API_URL = "";
    private final String API_KEY = "";

    public WeatherData getWeatherData(String location) {
        RestTemplate restTemplate = new RestTemplate();
        String url = API_URL + "?location=" + location + "&apiKey=" + API_KEY;

        WeatherData weatherData = restTemplate.getForObject(url, WeatherData.class);
        return weatherData;
    }
}
