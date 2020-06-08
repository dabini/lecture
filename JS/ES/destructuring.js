const name = "dabin"

const student = {
    name : '조다빈',
    age: 25,
    email: 'jdb960211@gmail.com',
    phone: '01012345678',
}

const { name } = student
const { age } = student
const { email } = student
const { phone } = student

console.log(name, age, email, phone)

function getStudentInfo(student) {
    console.log(`Hi, my name is ${student.name}, email is ${student.email}`)
}

getStudentInfo(student)

function getStudentInfo2({ name, age, email, phone}) {
    console.log(`Hi, my name is ${name}, email is ${email}`)
}


function saveStudent1(name, age, email, phone) {

}
saveStudent1('홍길동', 24, '123@email.com', )