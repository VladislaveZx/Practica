let tg = window.Telegram.WebApp;
let main = document.getElementById("main");
let doc_form = document.getElementById("doc-form");
let get_doc = document.getElementById("get-doc");
let accept = document.getElementById("accept");
let decline = document.getElementById("decline");
doc_form.style.display="none";

get_doc.addEventListener(
    "click", () => {
        doc_form.style.display="block";
        main.style.display="none";
        document.getElementById("studname").value = tg.initDataUnsafe.user.first_name + " " + tg.initDataUnsafe.user.last_name

    }
);

decline.addEventListener(
    "click", () => {
        tg.close();
    }
);

accept.addEventListener(
    "click", () => {
        let studnum = document.getElementById("studnum").value;
        let studname = document.getElementById("studname").value;
        let organisation = document.getElementById("organisation").value;
        if (studname.length < 5) {
            document.getElementById("error").innerText = "Ошибка в ФИО";
            return;
        }
        let document_data = {
            studnum: studnum,
            studname: studname,
            organisation: organisation
        }
        tg.sendData(JSON.stringify(document_data));
        tg.close();
    }
);