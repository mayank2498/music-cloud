function createlist(xmlhttp) {
    var text="";
    var xmlDoc = xmlhttp.responseXML;
    x = xmlDoc.getElementsByTagName("field");
    for(var i=0;i<x.length;i++){
        if(x[i].getAttribute("name")=="song_title"){
            text += "<h2>"+x[i].childNodes[0].nodeValue+"<br><br>";

        }
    }

    document.getElementById("song").innerHTML= text;
}

function process_search(url)
{
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            show_search_items(xmlhttp);
        }
    }
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
}

function process_album(url)
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            createlist(xmlhttp);
        }
    }
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
}

function display(pk) {

    xmlhttp = new XMLHttpRequest();
    if (pk < 0) {
        document.getElementById("song").innerHTML = "Move your mouse cursor over to an album image";
    }

    else {
        url = "http://127.0.0.1:8000/music/" + pk + "/fetchxml_forsongs";
        process_album(url);
    }
}


function getsearch_results(){
    url = "http://127.0.0.1:8000/music/fetchxml_foralbums";
    process_search(url);
    var node = document.getElementById("searched");
    clear(node);
}

function show_search_items(xmlhttp){
    var query = document.getElementById("search").value.toString().toLowerCase().trim();
    if (query.length>=2) {
        var xmldoc = xmlhttp.responseXML;
        var x = xmldoc.documentElement.childNodes;
        for (var i = 0; i < x.length; i++) {
            var pk = x[i].getAttribute("pk");
            var test_album = x[i].childNodes[2].childNodes[0].nodeValue.toLowerCase().trim();
            var test_artist = x[i].childNodes[1].childNodes[0].nodeValue.toLowerCase().trim();
            if ((test_album.indexOf(query) !== -1) || (test_artist.indexOf(query) !== -1)) {
                        albumname = x[i].childNodes[2].childNodes[0].nodeValue;
                        albumartist = x[i].childNodes[1].childNodes[0].nodeValue;
                       display_search(pk, albumname, albumartist);
            }
        }
    }
}


function  display_search(pk,test_album,test_artist) {
    var parent = document.getElementById("searched");
    var child = document.createElement("a");
    child.setAttribute("href","http://127.0.0.1:8000/music/"+pk);
    child.innerHTML = test_album + "<br>" ;
    parent.appendChild(child);
}

function clear(node){
    while (node.hasChildNo des()) {
        node.removeChild(node.lastChild);
    }
}

function get_song_search_results(){
    node = document.getElementById("searched_song");
    clear(node);
    url = "http://127.0.0.1:8000/music/fetchxml_forallsongs";
    process_song(url);
}
function process_song(url)
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            display_song(xmlhttp);
        }
    };
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
}
function display_song(xmlhttp){
    var query = document.getElementById("search_song").value.toString().toLowerCase().trim();
    if (query.length>=2) {
        var xmldoc = xmlhttp.responseXML;
        var x = xmldoc.documentElement.childNodes;
        for (var i = 0; i < x.length; i++) {
            var song_title = x[i].childNodes[2].childNodes[0].nodeValue.toLowerCase().trim();
            if (song_title.indexOf(query) !== -1) {
                song_title = x[i].childNodes[2].childNodes[0].nodeValue;
                display_search_songs(song_title,x[i].childNodes[1].childNodes[0].nodeValue.toString());
            }

        }
    }

}
function display_search_songs(song_title,file_name){
    var parent = document.getElementById("searched_song");
    var child = document.createElement("a");
    child.setAttribute("href","http://127.0.0.1:8000/media/"+file_name);
    child.innerHTML = song_title + "<br>" ;
    parent.appendChild(child);
}