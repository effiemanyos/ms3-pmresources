$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 5,
      maxDate: new Date(), // Set maximum date to "today"
      showClearBtn: true,
      i18n: {
        done:"select"
      }
    });
});

