$(document).ready(function() {
    window.model_catalog_table = $('#model_catalog_table').DataTable({
        dom: 'Bfrtip',
        buttons: [],
    });
});
async function getProductsData(id) {
    let records = [];
    await $.ajax({
        type: "GET",
        url: `/model-catalog/${id}/products/`,
        data: {},
        dataType: "json",
        success: async function(data){
            records = data;
            return data;
        },
        failure: function(errMsg) {
            console.log(errMsg);
            records = [];
        }
    });
    return records;
}

function format (data) {
    let table = `<table class="table table-bordered">`;
    let thead = `<thead class="thead-dark"><tr>`;
    for (let i = 0; i < data.columns.length; i++)  {
        thead += `<th>${data.columns[i]}</th>`;
    }
    thead += `</tr></thead>`;
    table += thead;
    let tBody = `<tbody>`;
    if (data.results.length === 0) {
        tBody += `<tr><td colspan="${data.columns.length}">No Data Available</td></tr>`;
    } else {
        for (let row = 0; row < data.results.length; row++) {
            let tRow = `<tr>`;
            for(let column = 0; column < data.columns.length; column++) {
                const columnName = data.columns[column];
                tRow += `<td>${data.results[row][columnName]}</td>`;
            }
            tRow += `</tr>`;
            tBody += tRow;
        }
    }
    tBody+= `</tbody>`;
    table += tBody;
    table += `</table>`;
    return table;
}

$('#model_catalog_table tbody').on('click', 'td.details-control', function() {
    var tr = $(this).closest('tr');
    var row = window.model_catalog_table.row( tr );
    if (row.child.isShown()) {
        // This row is already open - close it
        row.child.hide();
        tr.removeClass('shown');
    }
    else {
        // Open this row
        const id = row.data()[1];
        getProductsData(id).then((res) => {
            row.child(format(res)).show();
            tr.addClass('shown');
        });
    }
});

async function getModelCatalogReprocessConfirmationData(id) {
    let records = [];
    await $.ajax({
        type: "GET",
        url: `/model-catalog/reprocess-model-catalog/${id}/`,
        data: {},
        dataType: "json",
        success: async function(data){
            records = data;
            return data;
        },
        failure: function(errMsg) {
            console.log(errMsg);
            records = [];
        }
    });
    return records;
}

// $("#reprocessModel").on('show.bs.modal', function(){
//     let reprocess_selected_category_id = $("input[name=reprocess_selected_category]").val();
//     console.log(reprocess_selected_category_id);
//     if (reprocess_selected_category_id !== ""
//         && reprocess_selected_category_id !== null
//         && reprocess_selected_category_id !== undefined) {
//         getModelCatalogReprocessConfirmationData(reprocess_selected_category_id)
//             .then((response) => {
//                 console.log(response);
//             });
//     } else {
//         alert('Please select category to reprocess model catalog!');
//     }
// });

function openReprocessModal() {
    let reprocess_selected_category_id = $("input[name=reprocess_selected_category]").val();
    console.log(reprocess_selected_category_id);
    if (reprocess_selected_category_id !== ""
        && reprocess_selected_category_id !== null
        && reprocess_selected_category_id !== undefined) {
        $('#reprocessModel').modal('show');
        getModelCatalogReprocessConfirmationData(reprocess_selected_category_id)
            .then((response) => {
                console.log(response);
            });
    } else {
        alert('Please select category to reprocess model catalog!');
    }
}

function closeReprocessModal() {
    $('#reprocessModel').modal('hide');
}