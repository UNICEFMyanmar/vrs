(function redirect404Errors() {
    if (navigator.onLine) {
        window.location.replace("/offline/error");
    }
})();