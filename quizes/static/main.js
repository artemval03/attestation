console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Вы точно хотите начать проходить "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>сложность: <b>${difficulty}</b></li>
                <li>количество вопросов: <b>${numQuestions}</b></li>
                <li>score to pass: <b>${scoreToPass}%</b></li>
                <li>время: <b>${time} min</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))
