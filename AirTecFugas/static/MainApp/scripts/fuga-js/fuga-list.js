$(document).ready(
    function () {
        InitDataTable();
    });


function InitDataTable() {

    $('#TableFugaList').DataTable({
        'iDisplayLength': 10,
    });
}