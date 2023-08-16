<!-- PromptDisplay.svelte -->

<script>
    import {copyToClipboard} from './copy-util.js';

    export let prompt = '';

    function copyPrompt() {
        copyToClipboard(prompt);
    }
</script>

<div class="prompt-box">

    <div class="prompt-header">
        Generated Prompt
    </div>


    <div class="prompt-body">
        {@html prompt}
    </div>

    <button class="copy-button" on:click={copyPrompt}>
        Copy
    </button>

</div>


<style>
    .copy-button {
        position: relative;
        top: 0.5rem;
        right: 0.5rem;
    }

    .prompt-box {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 1rem;
    }

    .prompt-header {
        font-weight: bold;
        margin-bottom: 1rem;
    }

    .prompt-body {
        white-space: pre-wrap;
        background: #f9f9f9;
        padding: 1rem;
    }

</style>