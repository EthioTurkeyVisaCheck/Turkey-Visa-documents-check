<<<<<<< HEAD
documents.forEach(doc => {
    const div = document.createElement("div");
    div.innerHTML = `
        <label>${doc}</label>
        <div class="radio-group">
            <input type="radio" id="${doc}-have" name="${doc}" value="have" onclick="toggleUpload('${doc}')">
            <label for="${doc}-have" class="have">Have</label>

            <input type="radio" id="${doc}-no" name="${doc}" value="no" checked onclick="toggleUpload('${doc}')">
            <label for="${doc}-no" class="no">No</label>
        </div>
        <input type="file" class="upload" id="${doc}-upload">
    `;
    docContainer.appendChild(div);
=======
documents.forEach(doc => {
    const div = document.createElement("div");
    div.innerHTML = `
        <label>${doc}</label>
        <div class="radio-group">
            <input type="radio" id="${doc}-have" name="${doc}" value="have" onclick="toggleUpload('${doc}')">
            <label for="${doc}-have" class="have">Have</label>

            <input type="radio" id="${doc}-no" name="${doc}" value="no" checked onclick="toggleUpload('${doc}')">
            <label for="${doc}-no" class="no">No</label>
        </div>
        <input type="file" class="upload" id="${doc}-upload">
    `;
    docContainer.appendChild(div);
>>>>>>> 3f62b6a4e4f46d684f149e1e3746ca3867e07621
});