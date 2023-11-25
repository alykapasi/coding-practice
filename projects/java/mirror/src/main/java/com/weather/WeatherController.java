package com.weather;


@RestController
public class WeatherController {
    private final WeatherService weatherService;

    public WeatherController(WeatherService weatherService) {
        this.weatherService = weatherService;
    }

    @GetMapping("/weather")
    public WeatherData getWeather(@RequestParam String location) {
        return weatherService.getWeather(location);
    }
}
