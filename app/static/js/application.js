$(function(){

    // Set up PJAX.
    $('a[data-pjax]').pjax();
    //$('form[data-pjax]').pjax();
    var context = this;
    $(document).on('submit', 'form[data-pjax]', function (event) {
        var container = $(this).attr('data-pjax') || context;
        $.pjax.submit(event, container)
    });

    // Pretty print <pre> blocks.
    //prettyPrint();

});
