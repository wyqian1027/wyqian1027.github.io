//check off todos by clicking
$("ul").on("click", "li", function(){
	$(this).toggleClass("completed");
});


//delete Todo by clicking
$("ul").on("click", "span", function(event){
	$(this).parent().fadeOut(500, function(){
		$(this).remove(); // "this" refers to "this.parent"
	});
	event.stopPropagation(); // avoid event bubbling
});

$("input[type='text']").keypress(function(event){
	if(event.which === 13){
		//grabbing new text
		var todoText = $(this).val();
		$(this).val("");
		//create new li and add to ul
		$("ul").append("<li><span><i class='fas fa-trash-alt'></i></span> "+todoText+"</li>");
	}
});

$("#add").click(function(){
	$("input[type='text']").fadeToggle();
});