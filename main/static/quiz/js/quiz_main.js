console.log('hello world')
const modalBtns = [...document.getElementsByClassName('modal-btn')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const closeBtn = document.getElementById('close-button')

const modalOverlay = document.querySelector('.modal-overlay');

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')
    modalOverlay.style.display = 'flex';
    modalBody.innerHTML = `
        <div class="h5 mb-3">Вы точнго хотите начать "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>Сложность: <b>${difficulty}</b></li>
                <li>Количество вопросов: <b>${numQuestions}</b></li>
                <li>Для зачёта: <b>${scoreToPass}%</b></li>
                <li>Время: <b>${time} мин</b></li>
            </ul>
        </div>
    `


    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
    closeBtn.addEventListener('click', ()=>{
        modalOverlay.style.display = 'none'
    })
}))

// Получаем элементы модального окна
