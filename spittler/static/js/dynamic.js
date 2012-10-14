(function () {
    $(function showRandomSpittle() {
        $("#spittle-container").load("/spittler/spittle/random");
        setTimeout(showRandomSpittle, 3000);
    });
}).call(this);
