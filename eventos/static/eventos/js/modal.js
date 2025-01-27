function showModal(event, id) {
    event.preventDefault();

    // Crear el modal
    const modal = document.createElement('div');
    modal.classList.add('custom-modal');
    modal.innerHTML = `
        <div class="modal-content">
            <h2>Enviar Email</h2>
            <form method="post" enctype="multipart/form-data" action="/admin/eventos/evento/${id}/modal-enviar-email/">
                <input type="hidden" name="csrfmiddlewaretoken" value="${getCSRFToken()}">
                <label for="archivos">Seleccionar Archivos:</label>
                <input type="file" name="archivos" multiple><br><br>
                <button type="submit">Enviar Email</button>
                <button type="button" onclick="closeModal()">Cancelar</button>
            </form>
        </div>
        <div class="modal-backdrop" onclick="closeModal()"></div>
    `;

    document.body.appendChild(modal);
    document.querySelector('.custom-modal').classList.add('active');
    document.querySelector('.custom-modal-backdrop').classList.add('active');

    return false;
}

function closeModal() {
    const modal = document.querySelector('.custom-modal');
    if (modal) {
        modal.remove();
    }
}

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
