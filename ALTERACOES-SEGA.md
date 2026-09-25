# Alterações de identidade visual — SEGA

Este pacote já está com a personalização aplicada ao código. Não é necessário copiar trechos manualmente.

## Paleta aplicada

- Azul-marinho: `#112A55`
- Azul principal: `#0A5DC8`
- Verde: `#0FA85B`
- Amarelo: `#F8B109`

A paleta foi extraída visualmente da nova logo fornecida e organizada em variáveis CSS para facilitar manutenção.

## O que foi alterado

- Nome do sistema atualizado para **SEGA — Sistema de Gestão Acadêmica** em títulos, painel, rodapés, login, cadastro e páginas CRUD.
- Nova logo aplicada no cabeçalho público, rodapé, login e área administrativa.
- Ícone da marca aplicado na sidebar e favicons criados a partir da nova identidade.
- Página inicial ganhou cores, fundo, botões, cartões e destaques compatíveis com a marca.
- Login e cadastro foram harmonizados com a nova paleta.
- Dashboard administrativo, sidebar, botões, focos de formulário, indicadores e modo escuro foram personalizados.
- Cores-base do Eduleb e do AdminHMD também foram substituídas para que componentes adicionais mantenham a identidade do SEGA.
- Arquivos personalizados antigos com o prefixo `sga-` foram reorganizados como `sega-`.
- O JavaScript de formulários, que estava dentro da pasta `css`, foi movido para a pasta correta `static/sega/assets/js/`.
- Conflito de merge que ainda aparecia no final do `README.md` foi removido.

## Arquivos principais da identidade

```text
djangotutorial/static/sega/assets/
├── css/
│   ├── sega-admin.css
│   ├── sega-forms.css
│   └── sega-public.css
├── images/
│   ├── sega-favicon-32.png
│   ├── sega-favicon-64.png
│   ├── sega-icon.png
│   └── sega-logo.png
└── js/
    └── sega-forms.js
```

## Observação

A personalização foi feita sem alterar models, migrations, banco de dados, regras de permissão ou a lógica dos CRUDs. O foco foi identidade visual, nomenclatura e organização dos assets.
