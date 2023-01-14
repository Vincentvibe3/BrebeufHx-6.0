<script lang="ts">
	import {Button, Header, Navbar, Searchbar, Sidebar, SidebarLink, Spinner, TextArea, TextInput} from "nota-ui"
	import { env } from "$env/dynamic/public"

	export let sidebarOpen=false;

	let title=""
	let description=""
	let age=""
	let yearPublished=""
	let tagSearchText=""
	let tagsToAdd:string[] = []
	let pageCount=""
	let tagsAll =  [
		"tag 1", "tag 2", "tag 3","tag 4","tag 5","tag 6","tag 7","tag 8"
		,"tag 9","tag 10","tag 11","tag 12","tag 13", "tag 14", 
		"tag 15", "tag 16", "tag 17", "tag 18", "tag 19", "tag 20", "tag 21", 
		"tag 22", "tag 23", 
	]
	let tagsSuggest:string[] = []
	let postStatus = "none"
	let bookLength=""
	let lengthValid:boolean
	let author=""

	let numericalRegex = /^[0-9]+$/i

	const verifyBookLength = () => {
		let matchResult = bookLength.match(numericalRegex)
		lengthValid = matchResult!=null
	}

	const submitData = async () => {
		postStatus = "loading"
		let book = {
			name:title,
			desc:description,
			yearPublished:yearPublished,
			author:author,
			age:age,
			tags:tagsToAdd,
			length:pageCount
		}
		let response = await fetch(`${env.PUBLIC_API_SERVER}/add_book`, {
			method:"POST",
			mode:"cors",
			headers:{
				"Content-Type":"application/json"
			},
			body:JSON.stringify(book)
		})
		if (response.status!=200){
			postStatus="error"
		} else {
			postStatus="complete"
		}
	}


	const sortAlpha = (a:string, b:string) => {
		if (a < b) {
			return -1;
		}
		if (a > b) {
			return 1;
		}
		return 0;
	}

	const searchInput = (event: any) => {
		tagsSuggest = tagsAll.filter((value) => value.startsWith(event.detail.text));
	};

	const removeTag = (value:string) => {
		tagsAll.push(value)
		removeFromArray(tagsToAdd, value)
		tagsAll.sort(sortAlpha)
		tagsAll=tagsAll
		tagsToAdd=tagsToAdd
	}

	const removeFromArray = (tagArray:string[], value:string) =>{
		const index = tagArray.indexOf(value);
		if (index > -1) { // only splice array when item is found
			tagArray.splice(index, 1); // 2nd parameter means remove one item only
		}
	}

	const onTagSelected = (event:CustomEvent) => {
		tagsToAdd.push(event.detail.text)
		removeFromArray(tagsAll, event.detail.text)
		console.log(`removing ${event.detail.text}`)
		console.log(tagsAll)
		tagsAll.sort(sortAlpha)
		tagsAll=tagsAll
		tagsToAdd=tagsToAdd
		tagSearchText=""
	}

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
	img="https://images.unsplash.com/photo-1589998059171-988d887df646?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80">
	Add a book
</Header>
<main>
	<p>Title</p>
	<TextInput bind:text={title} placeholder="Title"></TextInput>
	<p>Author</p>
	<TextInput bind:text={author} placeholder="Author"></TextInput>
	<p>Target Age</p>
	<TextInput bind:text={age} placeholder="Age"></TextInput>
	<p>Page Count</p>
	<TextInput bind:text={pageCount} on:input={verifyBookLength} bind:valid={lengthValid} placeholder="Book Length"></TextInput>
	<p>Date Published</p>
	<TextInput bind:text={yearPublished} placeholder="Year published"></TextInput>
	<p>Description</p>
	<TextArea bind:text={description} placeholder="Description"></TextArea>
	<p>Tags</p>
	<Searchbar placeholder="Add a tag" bind:suggestions={tagsSuggest} on:optionClick={onTagSelected} on:input={searchInput} bind:text={tagSearchText}></Searchbar>
	<p>Added Tags</p>
	<div class="tagList">
		{#if tagsToAdd.length == 0}
			<p>No tags</p>
		{/if}
		{#each tagsToAdd as selectedTag}
			<div class="tagButtonWrapper">
				<Button type="secondary" on:click={()=>{removeTag(selectedTag)}}>
					<slot slot="icon">
						<svg xmlns="http://www.w3.org/2000/svg" width="192" height="192" viewBox="0 0 256 256"><rect width="256" height="256" stroke="none" fill="none"></rect><line x1="200" y1="56" x2="56" y2="200" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line><line x1="200" y1="200" x2="56" y2="56"stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line></svg>
					</slot>
					{selectedTag}
				</Button>
			</div>
		{/each}
	</div>
	<p>Finish</p>
	<Button on:click={submitData}>Submit</Button>
	{#if postStatus!="none"}
		<div class="statusWrapper">
			<Spinner bind:status={postStatus}></Spinner>
			{#if postStatus=="error"}
				<p>Something went wrong</p>
			{:else if postStatus=="complete"}
				<p>Done</p>
			{/if}
		</div>
	{/if}
</main>
<style>
	main {
		width: 80%;
		min-width: 30rem;
		margin: 2rem 2rem;
	}

	.tagList {
		width: 100%;
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
		justify-content: flex-start;
		margin: 1rem 0rem;
	}

	.tagList:global( svg ) {
		fill: var(--btnSecondaryIcon);
		stroke: var(--btnSecondaryIcon);
	}

	.statusWrapper {
		display: flex;
		flex-direction: row;
		align-items: center;
		width: fit-content;
		margin: 1rem 0rem;
	}

	.statusWrapper p {
		margin: 0px;
		margin-left: 1rem;
	}

	.tagButtonWrapper + .tagButtonWrapper {
		margin-left: 1rem;
	}

</style>