import 'bootstrap/dist/css/bootstrap.min.css'
import { Form, Row, Col } from 'react-bootstrap'
const Criteria = ({ description, id }) => {
    return (
        <div>
            <Form.Group controlId={id} as={Row}>
                    <Form.Check type="checkbox" label={description}></Form.Check>
            </Form.Group>
        </div>
    )
}

export default Criteria
