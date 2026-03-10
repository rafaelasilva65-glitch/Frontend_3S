// let nome = prompt("Como voce chama?")
//
// if (nome == null){
//     alert("Recarregue a página")
// } else {
//    let correto = confirm("Voce se chama" + nome + "?")
//
//     if (correto) {
//         alert(nome + "Bem Vindo ao site do nosso curso")
//     } else{
//         alert("Recarregue a página")
//     }
// }

function limpaInputsLogin() {
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputEmail.value = ''
    inputSenha.value = ''
}

function limpaInputsCadastroFuncionario() {
    const inputNome = document.getElementById('input-nome')
    const inputDataDeNacimento = document.getElementById('input-data_nascimento')
    const inputCpf = document.getElementById('input-cpf')
    const inputEmail1 = document.getElementById('input-email')
    const inputSenha1 = document.getElementById('input-senha')
    const inputCargo = document.getElementById('input-cargo')
    const inputSalario = document.getElementById('input-salario')

    inputNome.value = ''
    inputDataDeNacimento.value = ''
    inputCpf.value = ''
    inputEmail1.value = ''
    inputSenha1.value = ''
    inputCargo.value = ''
    inputSalario.value = ''
}
document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')
    const formCadastroFuncinonario = document.getElementById('form-cadastro_funcionario')

    formLogin.addEventListener("submit", function () {
        //Pegar os dois inputs do formulário
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')

        let temErro = false
        // verificar se os inputs estão vazios

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (temErro) {
            event.preventDefault()
            alert("Preencha todos os campos")
        }
    })

    formCadastroFuncinonario.addEventListener("submit", function (){
        const inputNome = document.getElementById('input-nome')
        const inputDataDeNascimento = document.getElementById('input-data_nascimento')
        const inputCpf = document.getElementById('input-cpf')
        const inputEmail1 = document.getElementById('input-email')
        const inputSenha1 = document.getElementById('input-senha')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        let temErro = false

        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }

        if (inputDataDeNascimento.value === '') {
            inputDataDeNascimento.classList.add('is-invalid')
            temErro = true
        } else {
            inputDataDeNascimento.classList.remove('is-invalid')
        }

        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }

        if (inputEmail1.value === '') {
            inputEmail1.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail1.classList.remove('is-invalid')
        }

        if (inputSenha1.value === '') {
            inputSenha1.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha1.classList.remove('is-invalid')
        }

        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }

        } )

        if (temErro) {
            event.preventDefault()
            alert("Preencha todos os campos")
        }


} )
