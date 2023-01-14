<script lang="ts">
	import {Header, Navbar, Sidebar, SidebarLink} from "nota-ui"
  	import BookForm from "./BookForm.svelte";

	export let sidebarOpen=false;

	const toggleSidebar = () => {
		sidebarOpen=true
	}
</script>
<Navbar on:onTitleClick={toggleSidebar} alwaysOpaque={false} style="top:0px; left:0px; z-index:2;">
	<div slot="icon" style="height: 40%; width:auto; margin:0rem; margin-right:1rem;">
		<svg style="height:100%; width:auto;" xmlns="http://www.w3.org/2000/svg" width="192" height="192" fill="#ffffff" viewBox="0 0 256 256"><rect width="256" height="256" fill="none"></rect><line x1="40" y1="128" x2="216" y2="128" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line><line x1="40" y1="64" x2="216" y2="64" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line><line x1="40" y1="192" x2="216" y2="192" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line></svg>
	</div>
	<div style="margin:0rem 1.5rem 0rem 1rem; width:100%; display: flex; flex-direction:row; align-items:center; justify-content:space-between;">
		
	</div>
</Navbar>
<Sidebar bind:show={sidebarOpen}>
	<SidebarLink href=".">Home</SidebarLink>
	<SidebarLink href="./login">Login</SidebarLink>
	<SidebarLink href="./library">Library</SidebarLink>
	<SidebarLink href="./addbook">Add Book</SidebarLink>
</Sidebar>
<Header
	img="https://images.unsplash.com/photo-1495446815901-a7297e633e8d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Ym9va3N8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60">
	Book Finder
</Header>
<main>
	<BookForm></BookForm>
</main>
<style>
	main {
		margin: 2rem 2rem;
	}

</style>