import React from "react";
import { Form, Button } from "semantic-ui-react";
import { useForm } from "react-hook-form";

function SiginPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <div>
      <Form onSubmit={handleSubmit(onSubmit)}>
        <Form.Field>
          <label>* User Name</label>
          <input
            placeholder="User Name"
            type="text"
            {...register("userName")}
          />
        </Form.Field>
        <Form.Field>
          <label>* Password</label>
          <input
            placeholder="Password"
            type="password"
            {...register("password")}
          />
        </Form.Field>
        <Button type="submit">Sign In</Button>
      </Form>
    </div>
  );
}

export default SiginPage;