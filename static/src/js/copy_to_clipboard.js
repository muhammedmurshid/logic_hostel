odoo.define('student_feedback.copy_to_clipboard', function (require) {
    "use strict";
    console.log('jhsdfgyeqyeuiqegdafhfagfgas')
    var core = require('web.core');
    var _t = core._t;

    // Register the button click event
    $(document).ready(function () {
        $(".action_done").on('click', function () {
        var fieldValue = $('#link').data('link');
        var valueToCopy = fieldValue; // Replace with the actual value

            // Create a hidden input element to facilitate copying
        var $tempInput = $("<input>");
        $("body").append($tempInput);
        $tempInput.val(valueToCopy).select();

            // Copy the value to the clipboard
        document.execCommand("copy");

            // Clean up by removing the temporary input element
        $tempInput.remove();

            // Provide user feedback (optional)
        alert(_t("Copied to clipboard: ") + valueToCopy);
       });



   });


            // Get the value you want to copy

});