const TextConvert = () => {
    let x = CKEDITOR.instances['id_body'].getData();
    //api de CKEDITOR
    let y = document.getElementById('htmldata');
    y.innerHTML = x;
}