//信息列表table控制隐藏弹出js

//Firefox 以及大多数其他的浏览器，会把节点间生成的空的空格或者换行当作文本节点，而 Internet Explorer 会忽略节点间生成的空白文本节点。
//函数来检查下一个同级节点的节点类型。
//元素节点的节点类型是 1，因此如果下一个同级节点不是一个元素节点，它就会移至下一个节点，然后继续检查此节点是否为元素节点。
//整个过程会一直持续到下一个同级元素节点被找到为止。
//通过这个方法，得到正确的结果。
function getNextSibling(nodeobj) {
	var o = nodeobj.nextSibling;
	while(o.nodeType != 1) {
		//		console.log(o.nodeType);
		o = o.nextSibling;
	}
	return o;
}



//<i class="fa fa-plus-square-o"></i><i class="fa fa-minus-square-o"></i>

window.onload = function() {
	var collape = document.getElementsByClassName('link-table-collape');
	for(var i = 0; i < collape.length; i++) {
		collape[i].addEventListener('click', function() {
			//			this.parentNode:链接所在的父元素,也就是+所在表格
			//			this.parentNode.parentNode:+所在表格的父元素,也就是tr
			//			this.parentNode.parentNode.parentNode就是tr的父元素了,tbody

			//			owIndex 属性返回某一行(rows )在表格的行集合中的位置（row index）。
			//			先算出点击链接所在的行
			//			var rowindex=this.parentNode.parentNode.rowIndex;
//			console.log(this.nodeName);
			var clpNode = getNextSibling(this.parentNode.parentNode);
			//clpNode.style.display="table-row";

			if(clpNode.style.display == "none" || clpNode.style.display == "") {
				for(var m = 0; m < document.getElementsByClassName('tr-collape').length; m++) {
					document.getElementsByClassName('tr-collape')[m].style.display = "none";
				}
				clpNode.style.display = "table-row";
				
				//链接+ -改变
				for(var n = 0; n < document.getElementsByClassName('fa-minus-square-o').length; n++) {
					document.getElementsByClassName('fa-minus-square-o')[n].setAttribute("class","fa fa-plus-square-o");
				}
				this.childNodes[1].setAttribute("class","fa fa-minus-square-o");
				
//				console.log(this.childNodes.length);
			} else {
				this.childNodes[1].setAttribute("class","fa fa-plus-square-o");
				clpNode.style.display = "none";
			}

		}, false);
	}
}