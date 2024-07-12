$(document).ready(function() {
    $('#weatherForm').on('submit', function(e) {
        e.preventDefault();
        let city = $('#city').val();

        $.ajax({
            url: `/weather/${city}/weather`,
            method: 'GET',
            success: function(response) {
                let weather = `
                    <h2>${response.name}, ${response.sys.country}</h2>
                    <p>Температура: ${response.main.temp} °C</p>
                    <p>Опис: ${response.weather[0].description}</p>
                    <p>Вологість: ${response.main.humidity}%</p>
                    <p>Швидкість вітру: ${response.wind.speed} м/с</p>
                `;
                $('#weatherResult').html(weather);
            },
            error: function() {
                $('#weatherResult').html('<p class="text-danger">Не вдалося отримати дані. Перевірте назву міста.</p>');
            }
        });
    });
});
