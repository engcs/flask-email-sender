function showAlert(){
  $("#barra_de_alerta").append(`
    <div class="alert alert-warning alert-dismissible teste fade show" style="display:show" role="alert" id="myAlert">
        <strong>Holy guacamole!</strong>
          <span id="myAlert2">
            You should check in on some of those fields below.
          </span>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
  `);
  $.each($('.teste'), function(index, element) {
    var t = setTimeout(function() {
        //element.setAttribute('style', 'display:none');
        //$(".alert").alert('close');
        $(element).fadeOut("fast")
    }, 3000);
  });

}

var exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
  var button = event.relatedTarget
  var recipient = button.getAttribute('data-id')
  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('#meu_id')
  modalTitle.textContent = 'Deletar registro ' + recipient
  modalBodyInput.value = recipient
  var btn = document.getElementById('btn-delete')
  btn.href = '/delete/' + recipient
})
