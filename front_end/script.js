// Função para gerar UUID
function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0;
        const v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

document.getElementById('infoForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    const uniqueIdentifier = generateUUID(); // Gera um novo UUID ao enviar o formulário
    document.getElementById('identifier').value = uniqueIdentifier; // Atualiza o campo identifier

    // Coletando os dados do formulário
    const formData = {
        identifier: uniqueIdentifier, // Usando o UUID gerado
        limite_credito: document.getElementById('limit_bal').value,
        sexo: document.getElementById('sex').value,
        escolaridade: document.getElementById('education').value,
        estado_civil: document.getElementById('marriage').value,
        idade: document.getElementById('age').value,
        status_pag_1: document.getElementById('pay_1').value,
        status_pag_2: document.getElementById('pay_2').value,
        status_pag_3: document.getElementById('pay_3').value,
        status_pag_4: document.getElementById('pay_4').value,
        status_pag_5: document.getElementById('pay_5').value,
        status_pag_6: document.getElementById('pay_6').value,
        fatura_1: document.getElementById('bill_amt1').value,
        fatura_2: document.getElementById('bill_amt2').value,
        fatura_3: document.getElementById('bill_amt3').value,
        fatura_4: document.getElementById('bill_amt4').value,
        fatura_5: document.getElementById('bill_amt5').value,
        fatura_6: document.getElementById('bill_amt6').value,
        pag_fatura_1: document.getElementById('pay_amt1').value,
        pag_fatura_2: document.getElementById('pay_amt2').value,
        pag_fatura_3: document.getElementById('pay_amt3').value,
        pag_fatura_4: document.getElementById('pay_amt4').value,
        pag_fatura_5: document.getElementById('pay_amt5').value,
        pag_fatura_6: document.getElementById('pay_amt6').value,
    };

    // Enviando os dados para o endpoint
    fetch('http://127.0.0.1:5000/application-score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na rede');
        }
        return response.json(); // Ou response.text() dependendo da resposta esperada
    })
    .then(data => {
        console.log('Sucesso:', data);

        // Exibir resultado da classificação
        const resultHTML = data.map(result => `
            <div class="container">
                <h2>Resultado da Classificação</h2>
                <table>
                    <tr>
                        <th>Identificador da Classificação</th>
                        <th>Probabilidade</th>
                        <th>Classe</th>
                    </tr>
                    <tr>
                        <td class="identifier">${result.identifier}</td>
                        <td class="probability">${result.prob_perc} %</td>
                        <td class="classify">${result.classify}</td>
                    </tr>
                </table>
            </div>
        `).join('');
        const imageHTML = data.map(result => `
            
            <div class="container">
                <h2>Explicação do Resultado</h2>
                <p><strong>Cores:</strong> As cores estão relacionadas com o aumento e diminuição da probabilidade de inadimplência de cada variável, azul representa diminuição e vermelho aumento, na probabilidade</p>
                <p><strong>Pesos:</strong> Já os valores das barras representam o peso de cada variável, quanto maior o número absoluto, mais sigificativo é a variável na classificação</p>
                <p><strong>Eixo y:</strong> No eixo y temos os valores das variáveis e no f(x) é a probabilidade de inadimplência calculada pelo modelo</p>
                <p><strong>Eixo x:</strong> No eixo x temos a escala de pesos das variáveis</p>
                <div  style="display: flex; justify-content: center;">
                    <img src="data:image/png;base64,${result.shap_plot}" alt="SHAP Plot" style="max-width: 100%; height: auto;" />
                </div>
            </div>
        `).join('');
        // // Exibir imagem base64 (se presente)
        // const imageHTML = data.shap_plot ? `
        //     <img src="data:image/png;base64,${data.shap_plot}" alt="SHAP Plot" style="max-width: 100%; height: auto;" />
        // ` : '';
        // Exibir imagem base64 (se presente)


        // Atualizar o conteúdo do resultado na página
        document.getElementById('result').innerHTML = resultHTML + imageHTML;
    })
    .catch((error) => {
        console.error('Erro:', error);
        // Exibir erro na página
        document.getElementById('result').innerHTML = `
            <strong>Resultado da Classificação (UUID):</strong> ${uniqueIdentifier}<br>
            <strong>Erro:</strong> ${error.message}
        `;
    });
});
