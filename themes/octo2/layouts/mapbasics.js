var myMap;

// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);

function init () {
    // Создание экземпляра карты и его привязка к контейнеру с
    // заданным id ("map"). &lon= &lon=
    myMap = new ymaps.Map('map', {
        // При инициализации карты обязательно нужно указать
        // её центр и коэффициент масштабирования.
        center: [54.922407, 43.352737], // Саров
        zoom: 14,
		controls: ['fullscreenControl', 'geolocationControl', 'rulerControl', 'searchControl', 'typeSelector', 'zoomControl']
    }, {
        searchControlProvider: 'yandex#search'
    });

  

}