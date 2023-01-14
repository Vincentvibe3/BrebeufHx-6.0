<script lang="ts">
	import {Header, Navbar, Sidebar, SidebarLink, Button} from "nota-ui"
  import { onMount } from "svelte";
  	import BookForm from "./BookForm.svelte";

	export let sidebarOpen=false;

	let loggedIn = false;

	onMount(()=>{
		loggedIn=document.cookie.includes("loggedIn=true")
	})

	const toggleSidebar = () => {
		sidebarOpen=true
	}

	const logOut = () =>{
		loggedIn=false
		document.cookie="loggedIn=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;"
	}
</script>
<Navbar on:onTitleClick={toggleSidebar} alwaysOpaque={false} style="top:0px; left:0px; z-index:2;">
	<div slot="icon" style="height: 40%; width:auto; margin:0rem; margin-right:1rem;">
		<svg style="height:100%; width:auto;" xmlns="http://www.w3.org/2000/svg" width="192" height="192" fill="#ffffff" viewBox="0 0 256 256"><rect width="256" height="256" fill="none"></rect><line x1="40" y1="128" x2="216" y2="128" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line><line x1="40" y1="64" x2="216" y2="64" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line><line x1="40" y1="192" x2="216" y2="192" stroke="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line></svg>
	</div>
	<svelte:fragment slot="title">
		Books
	</svelte:fragment>
	<div style="margin:0rem 1.5rem 0rem 1rem; width:100%; display: flex; flex-direction:row; align-items:center; justify-content:end;">
		{#if loggedIn}
			<Button on:click={logOut}>Logout</Button>
		{/if}
	</div>
</Navbar>
<Sidebar bind:show={sidebarOpen}>
	<SidebarLink href="/">Home</SidebarLink>
	<SidebarLink href="/library">Library</SidebarLink>
	{#if loggedIn}
		<SidebarLink href="/addbook">Add Book</SidebarLink>
	{:else}
		<SidebarLink href="/login">Login</SidebarLink>
		<SidebarLink href="/register">Register</SidebarLink>
	{/if}
</Sidebar>
<slot></slot>