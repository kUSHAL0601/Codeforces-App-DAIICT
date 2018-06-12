function gen()
{
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < 5; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    $('#msg').html(text);
}
function check()
{
	if(document.getElementById('msg').innerHTML==$('#chk').val())
	{
		window.location="http://192.168.43.42:8080/home"
	}
	else
	{
		alert('Please enter text correctly');
	}
}
