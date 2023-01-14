<script lang="ts">
	import {Button, Header, Navbar, Searchbar, Sidebar, SidebarLink, Spinner, TextArea, TextInput} from "nota-ui"
	import { env } from "$env/dynamic/public"
  import { onMount } from "svelte";

	export let sidebarOpen=false;

	let title=""
	let description=""
	let age=""
	let yearPublished=""
	let tagSearchText=""
	let tagsToAdd:string[] = []
	let pageCount=""
	let tagsAll:string[] =  []
	let tagsSuggest:string[] = tagsAll
	let postStatus = "none"
	let lengthValid:boolean
	let ageValid:boolean
	let yearValid:boolean
	let author=""
	let image=""

	let numericalRegex = /^[0-9]+$/i

	const verifyBookLength = () => {
		let matchResult = pageCount.match(numericalRegex)
		lengthValid = matchResult!=null
	}

	const verifyAge = () => {
		let matchResult = age.match(numericalRegex)
		ageValid = matchResult!=null
	}

	const verifyYear = () => {
		let matchResult = yearPublished.match(numericalRegex)
		yearValid = matchResult!=null
	}

	const submitData = async () => {
		postStatus = "loading"
		if (image==""){
			image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQiICxX7SNshiebtkyqGDBlFSsj6nd4pz7fIJcXwAc&s"
		}
		let book = {
			name:title,
			desc:description,
			yearPublished:yearPublished,
			author:author,
			age:age,
			tags:tagsToAdd,
			length:pageCount,
			image:image
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
		if (event.detail.text==""){
			tagsSuggest=tagsAll
		}
		tagsSuggest = tagsAll.filter((value) => value.toLowerCase().startsWith(event.detail.text.toLowerCase()));
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

	onMount(async ()=>{
		let response = await fetch(`${env.PUBLIC_API_SERVER}/get_tags`, {
			method:"GET"
		})
		tagsAll = JSON.parse(await response.text())
		if (!document.cookie.includes("loggedIn=true")){
			document.location="/"
		}
	})
</script>
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
	<TextInput bind:text={age} on:input={verifyAge} bind:valid={ageValid} placeholder="Age"></TextInput>
	<p>Page Count</p>
	<TextInput bind:text={pageCount} on:input={verifyBookLength} bind:valid={lengthValid} placeholder="Book Length"></TextInput>
	<p>Date Published</p>
	<TextInput bind:text={yearPublished} on:input={verifyYear} bind:valid={yearValid} placeholder="Year published"></TextInput>
	<p>Description</p>
	<TextArea bind:text={description} placeholder="Description"></TextArea>
	<p>Image</p>
	<TextArea bind:text={image} placeholder="Image"></TextArea>
	<p>Tags</p>
	<Searchbar placeholder="Add a tag" bind:suggestions={tagsSuggest} on:optionClick={onTagSelected} on:input={searchInput} bind:text={tagSearchText}></Searchbar>
	<p>Added Tags</p>
	<div class="tagList">
		{#if tagsToAdd.length == 0}
			<p style="margin-top:0px;">No tags</p>
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