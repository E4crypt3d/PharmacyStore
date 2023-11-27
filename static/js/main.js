"use strict";

/* Aside & Navbar: dropdowns */
Array.from(document.getElementsByClassName("dropdown")).forEach(function (elA) {
	elA.addEventListener("click", function (e) {
		if (e.currentTarget.classList.contains("navbar-item")) {
			e.currentTarget.classList.toggle("active");
		} else {
			var dropdownIcon = e.currentTarget.getElementsByClassName("mdi")[1];
			e.currentTarget.parentNode.classList.toggle("active");
			dropdownIcon.classList.toggle("mdi-plus");
			dropdownIcon.classList.toggle("mdi-minus");
		}
	});
});
/* Aside Mobile toggle */

Array.from(document.getElementsByClassName("mobile-aside-button")).forEach(
	function (el) {
		el.addEventListener("click", function (e) {
			var dropdownIcon = e.currentTarget
				.getElementsByClassName("icon")[0]
				.getElementsByClassName("mdi")[0];
			document.documentElement.classList.toggle("aside-mobile-expanded");
			dropdownIcon.classList.toggle("mdi-forwardburger");
			dropdownIcon.classList.toggle("mdi-backburger");
		});
	}
);
/* NavBar menu mobile toggle */

Array.from(document.getElementsByClassName("--jb-navbar-menu-toggle")).forEach(
	function (el) {
		el.addEventListener("click", function (e) {
			var dropdownIcon = e.currentTarget
				.getElementsByClassName("icon")[0]
				.getElementsByClassName("mdi")[0];
			document
				.getElementById(e.currentTarget.getAttribute("data-target"))
				.classList.toggle("active");
			dropdownIcon.classList.toggle("mdi-dots-vertical");
			dropdownIcon.classList.toggle("mdi-close");
		});
	}
);

/* Notification dismiss */

Array.from(
	document.getElementsByClassName("--jb-notification-dismiss")
).forEach(function (el) {
	el.addEventListener("click", function (e) {
		e.currentTarget.closest(".notification").classList.add("hidden");
	});
});
