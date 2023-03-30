import{S as q,i as A,s as D,a7 as I,e as w,a as T,t as E,b as d,d as j,f as g,g as k,l as K,h as F,n as m,c as v,m as C,j as y,k as G,o as S,C as L,F as P,Z as R,P as U,R as V,T as Z,I as z,O as H,U as J,V as M,L as N,K as Q}from"./index.4395ab38.js";function B(l,e,t){const s=l.slice();return s[10]=e[t],s}function W(l){let e;return{c(){e=E(l[3])},m(t,s){g(t,e,s)},p(t,s){s&8&&F(e,t[3])},d(t){t&&m(e)}}}function O(l){let e,t,s,c,o,u=l[10]+"",n,f,b,a;function r(){return l[8](l[10])}return{c(){e=w("label"),t=w("input"),c=T(),o=w("span"),n=E(u),t.disabled=l[2],t.checked=s=l[0].includes(l[10]),d(t,"type","checkbox"),d(t,"name","test"),d(t,"class","gr-check-radio gr-checkbox"),d(o,"class","ml-2"),d(e,"class",f="gr-input-label flex items-center text-gray-700 text-sm space-x-2 border py-1.5 px-3 rounded-lg cursor-pointer bg-white shadow-sm checked:shadow-inner "+l[5]),j(e,"!cursor-not-allowed",l[2])},m(h,i){g(h,e,i),k(e,t),k(e,c),k(e,o),k(o,n),b||(a=K(t,"change",r),b=!0)},p(h,i){l=h,i&4&&(t.disabled=l[2]),i&3&&s!==(s=l[0].includes(l[10]))&&(t.checked=s),i&2&&u!==(u=l[10]+"")&&F(n,u),i&32&&f!==(f="gr-input-label flex items-center text-gray-700 text-sm space-x-2 border py-1.5 px-3 rounded-lg cursor-pointer bg-white shadow-sm checked:shadow-inner "+l[5])&&d(e,"class",f),i&36&&j(e,"!cursor-not-allowed",l[2])},d(h){h&&m(e),b=!1,a()}}}function X(l){let e,t,s,c;e=new I({props:{show_label:l[4],$$slots:{default:[W]},$$scope:{ctx:l}}});let o=l[1],u=[];for(let n=0;n<o.length;n+=1)u[n]=O(B(l,o,n));return{c(){v(e.$$.fragment),t=T(),s=w("div");for(let n=0;n<u.length;n+=1)u[n].c();d(s,"class","flex flex-wrap gap-2"),d(s,"data-testid","checkbox-group")},m(n,f){C(e,n,f),g(n,t,f),g(n,s,f);for(let b=0;b<u.length;b+=1)u[b].m(s,null);c=!0},p(n,[f]){const b={};if(f&16&&(b.show_label=n[4]),f&8200&&(b.$$scope={dirty:f,ctx:n}),e.$set(b),f&103){o=n[1];let a;for(a=0;a<o.length;a+=1){const r=B(n,o,a);u[a]?u[a].p(r,f):(u[a]=O(r),u[a].c(),u[a].m(s,null))}for(;a<u.length;a+=1)u[a].d(1);u.length=o.length}},i(n){c||(y(e.$$.fragment,n),c=!0)},o(n){G(e.$$.fragment,n),c=!1},d(n){S(e,n),n&&m(t),n&&m(s),L(u,n)}}}function Y(l,e,t){let s,{value:c=[]}=e,{style:o={}}=e,{choices:u}=e,{disabled:n=!1}=e,{label:f}=e,{show_label:b}=e;const a=P(),r=i=>{c.includes(i)?c.splice(c.indexOf(i),1):c.push(i),a("change",c),t(0,c)},h=i=>r(i);return l.$$set=i=>{"value"in i&&t(0,c=i.value),"style"in i&&t(7,o=i.style),"choices"in i&&t(1,u=i.choices),"disabled"in i&&t(2,n=i.disabled),"label"in i&&t(3,f=i.label),"show_label"in i&&t(4,b=i.show_label)},l.$$.update=()=>{l.$$.dirty&128&&t(5,{item_container:s}=R(o,["item_container"]),s)},[c,u,n,f,b,s,r,o,h]}class p extends q{constructor(e){super(),A(this,e,Y,X,D,{value:0,style:7,choices:1,disabled:2,label:3,show_label:4})}}function x(l){let e,t,s,c,o;const u=[l[8]];let n={};for(let a=0;a<u.length;a+=1)n=V(n,u[a]);e=new Z({props:n});function f(a){l[9](a)}let b={choices:l[3],label:l[6],style:l[4],show_label:l[7],disabled:l[5]==="static"};return l[0]!==void 0&&(b.value=l[0]),s=new p({props:b}),z.push(()=>H(s,"value",f)),s.$on("change",l[10]),{c(){v(e.$$.fragment),t=T(),v(s.$$.fragment)},m(a,r){C(e,a,r),g(a,t,r),C(s,a,r),o=!0},p(a,r){const h=r&256?J(u,[M(a[8])]):{};e.$set(h);const i={};r&8&&(i.choices=a[3]),r&64&&(i.label=a[6]),r&16&&(i.style=a[4]),r&128&&(i.show_label=a[7]),r&32&&(i.disabled=a[5]==="static"),!c&&r&1&&(c=!0,i.value=a[0],N(()=>c=!1)),s.$set(i)},i(a){o||(y(e.$$.fragment,a),y(s.$$.fragment,a),o=!0)},o(a){G(e.$$.fragment,a),G(s.$$.fragment,a),o=!1},d(a){S(e,a),a&&m(t),S(s,a)}}}function $(l){let e,t;return e=new U({props:{visible:l[2],elem_id:l[1],type:"fieldset",disable:typeof l[4].container=="boolean"&&!l[4].container,$$slots:{default:[x]},$$scope:{ctx:l}}}),{c(){v(e.$$.fragment)},m(s,c){C(e,s,c),t=!0},p(s,[c]){const o={};c&4&&(o.visible=s[2]),c&2&&(o.elem_id=s[1]),c&16&&(o.disable=typeof s[4].container=="boolean"&&!s[4].container),c&2553&&(o.$$scope={dirty:c,ctx:s}),e.$set(o)},i(s){t||(y(e.$$.fragment,s),t=!0)},o(s){G(e.$$.fragment,s),t=!1},d(s){S(e,s)}}}function ee(l,e,t){let{elem_id:s=""}=e,{visible:c=!0}=e,{value:o=[]}=e,{choices:u}=e,{style:n={}}=e,{mode:f}=e,{label:b="Checkbox Group"}=e,{show_label:a}=e,{loading_status:r}=e;function h(_){o=_,t(0,o)}function i(_){Q.call(this,l,_)}return l.$$set=_=>{"elem_id"in _&&t(1,s=_.elem_id),"visible"in _&&t(2,c=_.visible),"value"in _&&t(0,o=_.value),"choices"in _&&t(3,u=_.choices),"style"in _&&t(4,n=_.style),"mode"in _&&t(5,f=_.mode),"label"in _&&t(6,b=_.label),"show_label"in _&&t(7,a=_.show_label),"loading_status"in _&&t(8,r=_.loading_status)},[o,s,c,u,n,f,b,a,r,h,i]}class le extends q{constructor(e){super(),A(this,e,ee,$,D,{elem_id:1,visible:2,value:0,choices:3,style:4,mode:5,label:6,show_label:7,loading_status:8})}}var se=le;const ae=["static","dynamic"],ne=l=>({type:"Array<string>",description:"list of selected choices",example_data:l.choices.length?[l.choices[0]]:[]});export{se as Component,ne as document,ae as modes};
//# sourceMappingURL=index.5309e46d.js.map
