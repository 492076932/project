

$(function () {

    // 加载左侧疾病分类
    // 定义一个函数 传入数据 在页面加载指定数量的疾病分类
    $.ajax({
        async: false,
        url:'/diseases/all',
        type:'get',
        dataType:'json',
        success:function(data){
        var html=''
        $.each(data,function(i,o){
            var disease=''
            disease+='<li class="sub"><a href="#" class="color-999 ">'
            disease+=`<span>${o.dname}</span>`
            disease+='<i class="verflag"></i><i class="cusfont cusfont-more"></i></a><div class="item"  style="z-index: 1;display: none"><div class="dept-list">'
            disease+='<div class="d-l">'

            $.each(o.dis_name,function(j,dn){
                disease+=`<a href="doctorsInfo/${o.id}" target="_blank" class="color-999">${dn[0]}</a>`
                disease+='<i class="verflag"></i>';
            })
            disease+='</div></div></div></li>';
           html+=disease
        })
        $('.disease-menu-list').append(html);

        }


    })

    $('.sub').bind("click",function(){
        $(this).attr("class","sub on");
        $(this).find("div").css("display","block");
        $('.item').css("z-index",1);
        $(this).find("div").css("z-index",5);
   })

//    $('.sub').bind("mouseover",function(){
//         $(this).attr("class","sub on");
//         $('.item').attr("display","none");
//         $(this).find("div").css("display","block");
////         $(this).find("div").css("z-index",5);
//       })



//    function add_diseases(data){
//        var html=''
//        $.each(data,function(i,o){
//            var disease=''
//            disease+='<li class="sub"><a href="#" class="color-999 ">'
//            disease+=`<span>${o.deptname}</span>`
//            disease+='<i class="verflag"></i><i class="cusfont cusfont-more"></i></a><div class="item"  style="display:none;"><div class="dept-list">'
//            disease+='<div class="dept-item clearfix"><div class="d-l">'
//
//            $.each(o.diseases,function(j,dn){
//                disease+=`<a href="doctorsInfo/${o.dept_id}" target="_blank" class="color-999">${dn.dis_name}</a>`
//                disease+='<i class="verflag"></i>';
//            })
//            disease+='</div></div></div></div></li>';
//           html+=disease
//        })
//        $('.disease-menu-list').append(html);
//    }
//
//    add_diseases(diseasedata)



//    $('.sub').bind("mouseover",function(){
//         $(this).attr("class","sub on");
//         $(this).find("div").css("display","block");
//    })

//    $('.sub').bind("mouseout",function(){
//         $(this).attr("class","sub");
//         var   item1=$('.sub  .item');
//         item1.css("display","none");
//    })




})