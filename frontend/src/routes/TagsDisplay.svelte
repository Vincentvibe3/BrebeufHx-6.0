<script lang="ts">
  import { Button } from "nota-ui";

	export let tags:string[]
	export let selectedTags:string[];

	const addTag = (value:string) =>{
		selectedTags.push(value)
		selectedTags=selectedTags
	}

	const removeTag = (value:string) =>{
		const index = selectedTags.indexOf(value);
		if (index > -1) { // only splice array when item is found
			selectedTags.splice(index, 1); // 2nd parameter means remove one item only
		}
		selectedTags=selectedTags
	}

</script>
<div class="container">
	{#each tags as tag}
		{#if selectedTags.includes(tag)}
			<Button style="margin:0.2rem; height:2.25rem;" type="secondary" on:click={()=>{removeTag(tag)}}>
				<slot slot="icon">
					<svg xmlns="http://www.w3.org/2000/svg" width="192" height="192" viewBox="0 0 256 256"><rect width="256" height="256" stroke="none" fill="none"></rect><line x1="200" y1="56" x2="56" y2="200" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line><line x1="200" y1="200" x2="56" y2="56"stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line></svg>
				</slot>
				{tag}
			</Button>
		{:else }
			<Button style="margin:0.2rem;" on:click={()=>{addTag(tag)}}>{tag}</Button>
		{/if}
	{/each }
</div>
<style>
	.container {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
		justify-content: center;
	}
	.container:global( svg ) {
		fill: var(--btnSecondaryIcon);
		stroke: var(--btnSecondaryIcon);
	}
</style>