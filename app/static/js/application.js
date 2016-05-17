$(function() {

  // Set up PJAX.
  $('a[data-pjax]').pjax();
  $('form[data-pjax]').pjax();

  //$('input[data-pjax]').pjax({type: "POST"});
  //$(document).pjax($('a[data-pjax]'));
  //$(document).pjax($('form[data-pjax]'));

  // Pretty print <pre> blocks.
  //prettyPrint();

});
