function code_output() {
	
	let el = document.createElement('div');
	el.classList.add('code-output');
	
	let btns_container = document.createElement('div');
	btns_container.classList.add('code-btn-container');
	el.appendChild(btns_container);
	
	let btn_run = document.createElement('div');
	btn_run.classList.add('code-btn', 'code-btn-play');
	btns_container.appendChild(btn_run);
	
	let btn_clear = document.createElement('div');
	btn_clear.classList.add('code-btn', 'code-btn-clear');
	btns_container.appendChild(btn_clear);
	
	let output = document.createElement('div');
	output.classList.add('code-output-text');
	el.appendChild(output);
	
	
	// ===================================
	btn_run.addEventListener('click', () => el.dispatchEvent(new Event('onPlay')));
	btn_clear.addEventListener('click', () => el.dispatchEvent(new Event('onClear')));
	
	el.output = output;
	el.attachEditor = (editor) => {
		let worker = null;
		
		el.addEventListener('onPlay', () => {
			if (!worker) {
				worker = lite_notebook.pyWorker;
				worker.addEventListener("print", (m) => {
					output.innerText += String(m.message).replace(/\\n/g, "<br>") + "\n";
					output.scrollTop = output.scrollHeight;
				});
				worker.run(editor.getValue(), {},
					(m) => {
						output.innerText += "process finished" + "\n";
						output.scrollTop = output.scrollHeight;
						worker.terminate();
						worker = null;
						btn_run.classList.remove('code-btn-stop');
						btn_run.classList.add('code-btn-play');
					},
					(m) => {
						output.innerText += m.replace(/\\n/g, "<br>") + "\n";
						output.scrollTop = output.scrollHeight;
						worker.terminate();
						worker = null;
						btn_run.classList.remove('code-btn-stop');
						btn_run.classList.add('code-btn-play');
					});
				btn_run.classList.remove('code-btn-play');
				btn_run.classList.add('code-btn-stop');
				output.innerText += "run...\n";
				output.scrollTop = output.scrollHeight;
			} else {
				btn_run.classList.remove('code-btn-stop');
				btn_run.classList.add('code-btn-play');
			}
		});
		el.addEventListener('onClear', () => output.innerText = "");
	};
	
	
	// ===================================
	return el;
}

export default code_output;
