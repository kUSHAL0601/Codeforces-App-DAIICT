$(document).ready(function() {
		window.location="http://192.168.43.42:8080/home#section1";

});
var pg_no=1;
var user_id='R.I.P_kUSHAL';
function load_info(cf_id)
{
    $.ajax({
	url:'http://192.168.43.42:8080/getinfo',
	method:'POST',
	data:{codeforces_id:cf_id,pg_no:pg_no},
	success:function(response)
	{
		console.log(response);
		arr=response.result;
		document.getElementById('tb').innerHTML="";
		for(var i=0;i<(response.result).length;i++)
		{
			if((arr[i].pno).length==4){
			document.getElementById('tb').innerHTML+="<tr id=\""+arr[i].soln_id+"\"><td><a target=\"blank\" href=\"http://codeforces.com/problemset/problem/"+(arr[i].pno).charAt(0)+(arr[i].pno).charAt(1)+(arr[i].pno).charAt(2)+"/"+(arr[i].pno).charAt(3)+"\">"+arr[i].pno+"</a></td><td colspan=\"2\">"+arr[i].pnm+"</td><td>"+arr[i].date+"</td><td>"+arr[i].time+"</td><td>"+arr[i].memory+"</td><td>"+arr[i].lang+"</td><td>"+arr[i].status+"</td><td><a target='blank' href=\"http://codeforces.com/contest/"+(arr[i].pno).charAt(0)+(arr[i].pno).charAt(1)+(arr[i].pno).charAt(2)+"/submission/"+arr[i].soln_id+"\">Submiited Soln</a></td></tr>";
		}	if((arr[i].pno).length==3){
			document.getElementById('tb').innerHTML+="<tr id=\""+arr[i].soln_id+"\"><td><a target=\"blank\" href=\"http://codeforces.com/problemset/problem/"+(arr[i].pno).charAt(0)+(arr[i].pno).charAt(1)+"/"+(arr[i].pno).charAt(2)+"\">"+arr[i].pno+"</a></td><td colspan=\"2\">"+arr[i].pnm+"</td><td>"+arr[i].date+"</td><td>"+arr[i].time+"</td><td>"+arr[i].memory+"</td><td>"+arr[i].lang+"</td><td>"+arr[i].status+"</td><td><a target='blank' href=\"http://codeforces.com/contest/"+(arr[i].pno).charAt(0)+(arr[i].pno).charAt(1)+"/submission/"+arr[i].soln_id+"\">Submiited Soln</a></td></tr>";
		}
					if((arr[i].pno).length==2){
			document.getElementById('tb').innerHTML+="<tr id=\""+arr[i].soln_id+"\"><td><a target=\"blank\" href=\"http://codeforces.com/problemset/problem/"+(arr[i].pno).charAt(0)+"/"+(arr[i].pno).charAt(1)+"\">"+arr[i].pno+"</a></td><td colspan=\"2\">"+arr[i].pnm+"</td><td>"+arr[i].date+"</td><td>"+arr[i].time+"</td><td>"+arr[i].memory+"</td><td>"+arr[i].lang+"</td><td>"+arr[i].status+"</td><td><a target='blank' href=\"http://codeforces.com/contest/"+(arr[i].pno).charAt(0)+"/submission/"+arr[i].soln_id+"\">Submiited Soln</a></td></tr>";
		}
		}
		window.location="http://192.168.43.42:8080/home#section1";
		$('#btr').show();
	},
	error: function(response)
	{
	    alert('Check your Internet connection');
	},
    });
}

load_info('R.I.P_kUSHAL',1);
function search() {
	$('#btr').hide();
	pg_no=1;
	user_id=$('#srch_nm').val();
	load_info($('#srch_nm').val());
	console.log('Search Enterred');
}
function next()
{
	pg_no++;
	load_info(user_id);
}
function prev()
{
	if(pg_no>1)
{		pg_no--;
	load_info(user_id);
}
else
		window.location="http://192.168.43.42:8080/home#section1"

}
