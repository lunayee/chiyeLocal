function MyTable(myTableID) {
    var myTable = document.body.querySelector(myTableID);
    var head = myTable.querySelector(".myTable_head");
    var headContent = head.querySelector("* > .myTable_headContent");
    var content = myTable.querySelector(".myTable_content");

    function update(myTable) {
        var headItems = head.querySelectorAll("* > .headItems > .headItem");
        var styleWidths = content.querySelectorAll(".styleWidth > td");

        headItems.forEach(function(headItem, index) {
            var rect = headItem.getBoundingClientRect();
            styleWidths[index].style.minWidth = `${rect.width}px`;
            /*styleWidths[index].style.maxWidth = `${rect.width}px`;*/
        });
    }

    function scroll() {
        headContent.scrollLeft = content.scrollLeft;
    }

    function resize() {
        update(myTable);
    }
    content.addEventListener("scroll", scroll);
    window.addEventListener("resize", resize);
    this.update = function() {
        update(myTable);
    }
    this.remove = function() {
        content.removeEventListener("scroll", scroll);
        window.removeEventListener("resize", resize);
    };
}
