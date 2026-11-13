// JavaScript complementar do ClinicaApp (carregado em templates/base.html)
document.addEventListener('DOMContentLoaded', function () {
    // Fecha automaticamente as mensagens de alerta depois de 5 segundos.
    document.querySelectorAll('.alert-dismissible').forEach(function (alerta) {
        setTimeout(function () {
            if (window.bootstrap && bootstrap.Alert) {
                bootstrap.Alert.getOrCreateInstance(alerta).close();
            }
        }, 5000);
    });
});
