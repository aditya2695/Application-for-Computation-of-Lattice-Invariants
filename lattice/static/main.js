
function navTextControl(link_no){

    if(link_no==1){

    }



}



function clear2D(){

    $('#len_a1').val('')
    $('#len_b1').val('')
    $('#angle1').val('')
    $('#len_a2').val('')
    $('#len_b2').val('')
    $('#angle2').val('')

}

function compareCIF(){

    // files = getMediaFiles()

    // console.log(files)

    $.ajax({
        type:'POST',
        url:'/lattice/compareCIFs',
        data:{},
        success:function(response){
            console.log(response)
            document.getElementById('up_coform_val').innerHTML=response

        }
    })

}

function computeDistMatrix(){

    // files = getMediaFiles()

    // console.log(files)

    $.ajax({
        type:'POST',
        url:'/lattice/computeDistMatrix',
        data:{},
        success:function(response){
            console.log(response)
            document.getElementById('up_coform_val').innerHTML=response

        }
    })

}


function removeFile(file_name){

    console.log(file_name)
    var r=confirm("Are you sure you want to remove the file ?");
						
    if (r==true){
        
        var data = new FormData();
    data.append("file",file_name );
    data.append("csrfmiddlewaretoken", "{{ csrf_token }}");

    console.log(data)

    $.ajax({
        method:'POST',
        url:'/lattice/remove_file',
        data:data,
        processData: false,
        contentType: false,
        success:function(response){
            

            // files=getMediaFiles()
            
            // console.log('f:',list(files))
            // createFileList(files)


            // hiding removed file
            var li = document.getElementById(file_name)
            li.style.display = "none";

            
            

        }
    })



    }

    

}


function getMediaFiles(){

    $.ajax({
        method: "POST",
        url: "/lattice/getMediaFiles",
        processData: false,
        contentType: false,
    
        data: {'file':123},
        success: function(res) {
            console.log('res:',res)
            
            files = res.files
            console.log('files:',files)
            return res
        }
    })


}

function createFileList(files){

    console.log('create')
    var div = document.getElementById("file_list");
    while(div.firstChild){
        div.removeChild(div.firstChild);
    }
    var ul=document.createElement('ul');
    ul.classList.add("listbox");

    html_content='<p>'+ "Uploaded files" + '</p>'+
                '<ul id="myUL" class="listbox w20 h25" data-selectbox tabindex="-1" style="border-width:2px,border-radius:10px;overflow-y:auto;">'
                    

    for (var i = 0; i < files.length; i++) { 

        html_content=html_content+' <li id="'+files[i]+'" class="listitem "  ><span>'+files[i] +'<a title="Remove "  onclick=removeFile("'+files[i]+'")>'+
        '<i class="Small material-icons">delete_forever</i></a></span></li>'

    

    }

    html_content = html_content+'</ul>'

    document.getElementById("file_list").innerHTML = html_content
}
    // for (var i = 0; i < files.length; i++) { 

    //     console.log(files[i])
    //     var li=document.createElement('li');
    //     li.classList.add("listitem");
    //     var txt = document.createTextNode(files[i]);
    //     li.appendChild(txt);
    //     ul.appendChild(li)

    // }


// file upload operation 
function uploadClusterFile() {
    var data = new FormData();
    data.append("file", $("input[id^='file_cluster']")[0].files[0]);
    data.append("csrfmiddlewaretoken", "{{ csrf_token }}");
    console.log(data.size)
    $.ajax({
        method: "POST",
        url: "/lattice/upload_file",
        processData: false,
        contentType: false,
        mimeType: "multipart/form-data",
        data: data,
        success: function(res) {
            console.log(res)
            const file_objs = JSON.parse(res)
            files = file_objs.files
            console.log(files)
            createFileList(files)
        }
    })
}




// file upload operation 
function uploadFile() {
    var data = new FormData();
    data.append("file", $("input[id^='file']")[0].files[0]);
    data.append("csrfmiddlewaretoken", "{{ csrf_token }}");
    console.log(data.size)
    $.ajax({
        method: "POST",
        url: "/lattice/upload_file",
        processData: false,
        contentType: false,
        mimeType: "multipart/form-data",
        data: data,
        success: function(res) {
            console.log(res)
            const file_objs = JSON.parse(res)
            files = file_objs.files
            console.log(files)
            createFileList(files)
        }
    })
}









// 2d lattice entry
$(document).on('submit','#2d_lattice_form',function(e){
    e.preventDefault();//prevent refresh

    console.log($('#len_a').val())

    $.ajax({
        type:'POST',
        url:'/lattice/compute2d',
        data:{
            len_a1:$('#len_a1').val(),
            len_b1:$('#len_b1').val(),
            angle1:$('#angle1').val(),
            len_a2:$('#len_a2').val(),
            len_b2:$('#len_b2').val(),
            angle2:$('#angle2').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(response){
            console.log(response)
            document.getElementById('2d_dist').textContent =response

        }
    })

})

// // 3d lattice entry
// $(document).on('submit','#3d_lattice_form1',function(e){
//     e.preventDefault();//prevent refresh

//     console.log(123)

//     lat1 = $('#a_1').val().split(",");
//     lat2 = $('#a_2').val().split(",");

//     console.log($('#a_1').val())
//     console.log($('#a_2').val())

//     $.ajax({
//         type:'POST',
//         url:'/lattice/compute3d',
//         data:{
//             a1:lat1[0],
//             b1:lat1[1],
//             c1:lat1[2],
//             alpha1:lat1[3],
//             beta1:lat1[4],
//             gamma1:lat1[5],

//             a2:lat1[0],
//             b2:lat1[1],
//             c2:lat1[2],
//             alpha2:lat1[3],
//             beta2:lat1[4],
//             gamma2:lat1[5],
//             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//         },
//         success:function(response){
//             console.log(response)
//             document.getElementById('3d_dist').textContent ='3D Coform Distance:'+response

//         }
//     })

// })

// // 3d lattice entry
// $(document).on('submit','#3d_lattice_form2',function(e){
//     e.preventDefault();//prevent refresh

//     console.log($('#a_1').val())

//     $.ajax({
//         type:'POST',
//         url:'/lattice/compute3d',
//         data:{
//             a1:$('#a_1').val(),
//             b1:$('#b_1').val(),
//             c1:$('#c_1').val(),
//             alpha1:$('#alpha_1').val(),
//             beta1:$('#beta_1').val(),
//             gamma1:$('#gamma_1').val(),

//             a2:$('#a_2').val(),
//             b2:$('#b_2').val(),
//             c2:$('#c_2').val(),
//             alpha2:$('#alpha_2').val(),
//             beta2:$('#beta_2').val(),
//             gamma2:$('#gamma_2').val(),
//             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//         },
//         success:function(response){
//             console.log(response)
//             document.getElementById('3d_dist').textContent ='3D Coform Distance:'+response

//         }
//     })

// })

// file upload operation 
function form3d(view_type) {

    console.log('view_type:',view_type)

    if(view_type==1){


        lat1 = $('#a_1').val().split(",");
        lat2 = $('#a_2').val().split(",");

        
        $.ajax({
            type:'POST',
            url:'/lattice/compute3d',
            data:{
                a1:lat1[0],
                b1:lat1[1],
                c1:lat1[2],
                alpha1:lat1[3],
                beta1:lat1[4],
                gamma1:lat1[5],
    
                a2:lat2[0],
                b2:lat2[1],
                c2:lat2[2],
                alpha2:lat2[3],
                beta2:lat2[4],
                gamma2:lat2[5],
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(response){
                console.log(response)
                document.getElementById('3d_dist').textContent =response
    
            }
        })
    }

    else{
        $.ajax({
            type:'POST',
            url:'/lattice/compute3d',
            data:{
                a1:$('#a_1').val(),
                b1:$('#b_1').val(),
                c1:$('#c_1').val(),
                alpha1:$('#alpha_1').val(),
                beta1:$('#beta_1').val(),
                gamma1:$('#gamma_1').val(),
    
                a2:$('#a_2').val(),
                b2:$('#b_2').val(),
                c2:$('#c_2').val(),
                alpha2:$('#alpha_2').val(),
                beta2:$('#beta_2').val(),
                gamma2:$('#gamma_2').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(response){
                console.log(response)
                document.getElementById('3d_dist').textContent =response
    
            }
        })
    }

    
}

function viewChange(val){

    if(val==2){
        console.log(val)


        html_content1 = 
        
        
        '<br><h5 style="font-family: Montserrat, sans-serif;font-weight: normal;">Lattice 1</h5>'+


            
        '<label for="exampleFormControlInput1">a</label>'+
       '<input  class="form-control ip_2d" id="a_1" placeholder="Enter value of a">'+

        '<label for="exampleFormControlInput1">b</label>'+
        '<input  class="form-control ip_2d" id="b_1" placeholder="Enter value of b">'+

        '<label for="exampleFormControlInput1">c</label>'+
        '<input  class="form-control ip_2d" id="c_1" placeholder="Enter value of c">'+

        '<label for="exampleFormControlInput1">alpha</label>'+
        '<input  class="form-control ip_2d" id="alpha_1" placeholder="Enter value of alpha">'+

        '<label for="exampleFormControlInput1">beta</label>'+
        '<input  class="form-control ip_2d" id="beta_1" placeholder="Enter value of beta">'+

        '<label for="exampleFormControlInput1">gamma</label>'+
        '<input  class="form-control ip_2d" id="gamma_1" placeholder="Enter value of beta">'

        html_content2 = '<br><h5 style="font-family: Montserrat, sans-serif;font-weight: normal;">Lattice 2</h5>'+
            
        '<label for="exampleFormControlInput1">a</label>'+
       '<input  class="form-control ip_2d" id="a_2" placeholder="Enter value of a">'+

        '<label for="exampleFormControlInput1">b</label>'+
        '<input  class="form-control ip_2d" id="b_2" placeholder="Enter value of b">'+

        '<label for="exampleFormControlInput1">c</label>'+
        '<input  class="form-control ip_2d" id="c_2" placeholder="Enter value of c">'+

        '<label for="exampleFormControlInput1">alpha</label>'+
        '<input  class="form-control ip_2d" id="alpha_2" placeholder="Enter value of alpha">'+

        '<label for="exampleFormControlInput1">beta</label>'+
        '<input  class="form-control ip_2d" id="beta_2" placeholder="Enter value of beta">'+

        '<label for="exampleFormControlInput1">gamma</label>'+
        '<input  class="form-control ip_2d" id="gamma_2" placeholder="Enter value of beta"><br>'

        // form_prop = '<form id="3d_lattice_form2" method="POST" >'

        submit_html = '<input class="btn btn-primary"  type="button" onclick="clear3D(2)" value="Clear" />'+
                        '<input class="btn btn-secondary" type="submit" value="Submit" onclick="form3d(2)" />'

        document.getElementById("lat1_3d").innerHTML = html_content1
        document.getElementById("lat2_3d").innerHTML = html_content2
        document.getElementById("btn_3d").innerHTML = submit_html


    }
    else{
        

        html_content1 = '<p style="font-family: Montserrat, sans-serif;font-weight: normal;"> Enter the 3D lattice parameters separated by commas in the order a, b, c, α, β, γ  </p>'+
    

        '<br><h5 style="font-family: Montserrat, sans-serif;font-weight: normal;">Lattice 1</h5>'+
            
       '<input  class="form-control ip_2d" id="a_1" placeholder="Enter value of params">'

       html_content2 = '<h5 style="font-family: Montserrat, sans-serif;font-weight: normal;">Lattice 2</h5>'+
            
    
       '<input  class="form-control ip_2d" id="a_2" placeholder="Enter value of params"><br>'

    //    form_prop = '<form id="3d_lattice_form1" method="POST" >'

       submit_html = '<input class="btn btn-primary"  type="button" onclick="clear3D(1)" value="Clear" />'+
                        '<input class="btn btn-secondary" type="submit" value="Submit" onclick="form3d(1)" />'

        document.getElementById("lat1_3d").innerHTML = html_content1
        document.getElementById("lat2_3d").innerHTML = html_content2
        document.getElementById("btn_3d").innerHTML = submit_html

    }


}





const modalBody = document.getElementById('modal-body')

