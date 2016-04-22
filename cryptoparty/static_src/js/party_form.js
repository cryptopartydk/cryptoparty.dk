$(function () {
  $('#adresse-autocomplete').dawaautocomplete({
    error: function (xhr, status, error) {
      alert('Der opstod en fejl: ' + status + " - " + error);
      console.log(xhr)
    }
  });

  $('#start-group .input-group').datetimepicker({
    'defaultDate': $('#id_start').val(),
    'format': 'YYYY-MM-DD HH:mm'
  });

  $('#end-group .input-group').datetimepicker({
    'defaultDate': $('#id_end').val(),
    'format': 'YYYY-MM-DD HH:mm'
  });
});
