window.addEventListener("load", function () {
  $("#loading").delay(1000).fadeOut(3000);
  $("#loading_css").delay(2000).fadeOut(3000);

  var myTableC = new MyTable("#myTable");
  var StartTime = document.getElementById("StartTime");
  var EndTime = document.getElementById("EndTime");
  var table1_0 = document.getElementById("table1_0");

  var SwitchCheck_all = {};
  var SwitchCheck = document.querySelectorAll("input[type=checkbox]");
  SwitchCheck.forEach(function (d) {
    SwitchCheck_all[d.value] = [d.placeholder.toString(), d.checked.toString()];
  });

  var page = 1;
  var count = 1440;
  var totalPage = 0;
  var now = moment();
  var stv = now.clone().add(-1, "days").format("YYYY-MM-DD 00:00");
  var etv = now.clone().add(1, "hours").format("YYYY-MM-DD HH:00");

  updateTable(StartTime.value, EndTime.value, page, count);

  $("#StartTime").datetimepicker({
    timepicker: true,
    datepicker: true,
    format: "Y-m-d H:i",
    value: stv,
    /*onShow:function(ct){
          this.setOptions({
            maxDate:$('#EndTime').val() ? $('#EndTime').val() : false
          })
        }*/
  });
  $("#EndTime").datetimepicker({
    timepicker: true,
    datepicker: true,
    format: "Y-m-d H:i",
    value: etv,
    onShow: function (ct) {
      this.setOptions({
        minDate: $("#StartTime").val() ? $("#StartTime").val() : false,
      });
    },
  });

  const Toast = Swal.mixin({
    toast: true,
    position: "top",
    showConfirmButton: false,
    timer: 3000,
    onOpen: (toast) => {
      toast.addEventListener("mouseenter", Swal.stopTimer);
      toast.addEventListener("mouseleave", Swal.resumeTimer);
    },
  });

  $("#prevbtn").on("click", function () {
    if (page <= 1) return;
    page--;
    updateTable(StartTime.value, EndTime.value, page, count);
  });
  $("#nextbtn").on("click", function () {
    if (page >= totalPage) return;
    page++;
    updateTable(StartTime.value, EndTime.value, page, count);
  });

  function updateTable(st, et, page, count) {
    var myTable = document.getElementById("myTable");
    var historytbody = myTable.querySelector(".historytbody");
    var headItems = myTable.querySelector(".headItems");

    var SwitchCheck_all = {};
    var SwitchCheck = document.querySelectorAll("input[type=checkbox]");

    SwitchCheck.forEach(function (d) {
      SwitchCheck_all[d.value] = [d.placeholder.toString(), d.checked.toString()];
    });

    axios
      .get("/getHistory/", {
        params: {
          st: st,
          et: et,
          page: page,
          count: count,
          table: table1_0.value,
          SwitchCheck_all: SwitchCheck_all,
        },
      })
      .then(function (resp) {
        return resp.data;
      })
      .then(function (data) {
        var nameitems = "";
        nameitems += `
			  <div class="headItem table_id">ID</div>
			  <div class="headItem table_date_time">Date_time</div>`;

        data.check[1].forEach(function (el) {
          nameitems += `			  
			  <div class="headItem table_item">${el}</div>
			  `;
              
        });
        

        var items = "";

        data.list.forEach(function (el, index) {
          var name = "";
          data.check[0].forEach(function (itemname) {
            name += `
				  <td class="fw-bold">${el[itemname]}</td>`;
          });

          items += `
              <tr>
                <td class="fw-bold">${(page - 1) * count + index + 1}</td>
                <td class="fw-bold">${el.Date_Time}</td>
                ${name}
              </tr>
            `;
        });
        var b = "";
        for (var i = 0; i < data.check[0].length + 2; i++) {
          b += `<td></td>`;
        }
        var h = `
              <tr class="styleWidth">                
				${b}
              </tr>
            `;

        historytbody.innerHTML = h + items;
        headItems.innerHTML = nameitems;
        myTableC.update();
        totalPage = data.totalPage;
        $("#loading").hide();
        $("#loading_css").hide();
      });
  }

  savebtn.addEventListener("click", function () {
    page = 1;
    $("#loading").show();
    $("#loading_css").show();
    updateTable(StartTime.value, EndTime.value, page, count);
  });
  exportbtn.addEventListener("click", function () {
    axios.get("/GetExport/", { params: { st: StartTime.value, et: EndTime.value, table: table1_0.value, SwitchCheck_all: SwitchCheck_all } }).then(function (resp) {
      Toast.fire({
        icon: "success",
        title: "Export成功！",
      });
    });
  });
  backupbtn.addEventListener("click", function () {
    axios.get("/recover/", { params: { st: StartTime.value, et: EndTime.value, table: table1_0.value } })
    .then(function(resp){
            Toast.fire({
                icon: 'success',
                title: '回補成功！'
              })
        })
        .catch(function(resp){
            Toast.fire({
                icon: 'error',
                title: '回補失敗！'
              })
            console.log(err);
        })
    
  });
  
});