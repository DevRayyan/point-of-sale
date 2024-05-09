$('#checkbox-all').change(function () {
    $(".checkbox").attr('checked', $(this).is(":checked"));
});


$(".dismiss-alert").click(function () {
    $("#success-alert").hide(); 
    $("#danger-alert").hide(); 
});