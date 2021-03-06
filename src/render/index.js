import iomd from "./iomd.js";
import css_parser from "./css.js";
import js_parser from "./js.js";
import fetch_parser from "./ftch.js";
import md_parser from "./md.js";
import py_parser from "./py.js";
import editor_parser from "./editor.js";


const parsers = [
	css_parser,
	js_parser,
	fetch_parser,
	md_parser,
	//py_parser,
	editor_parser
];


export async function renderMD(md, element) {
	let chunks = iomd.parse(md);
	
	for (let i = 0; i < chunks.length; i++) {
		let ch = chunks[i];
		if (!ch.type) continue;
		
		let type = ch.type.trim().toLowerCase();
		
		let parser = parsers.find(p => p.types.indexOf(type) >= 0);
		if (parser) await parser.parse(ch, element);
	}
}
