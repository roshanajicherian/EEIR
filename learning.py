import tensorflow as tf
def neural(weight_list,z_list,e_list, demands_dict,graph):
    # Define the input placeholders
    tf.compat.v1.disable_eager_execution()
    weight = tf.compat.v1.placeholder(tf.float32, shape=[None, 1], name='weight')
    z_value = tf.compat.v1.placeholder(tf.float32, shape=[None, 1], name='z_value')
    e_value = tf.compat.v1.placeholder(tf.float32, shape=[None, 1], name='e_value')

    #Obtaining training and testing dataset
    print(weight_list)
    divider = int(len(weight_list)*0.8)
    weight_train = weight_list[:divider]
    weight_test = weight_list[divider+1:]
    z_value_train = z_list[:divider]
    z_value_test = z_list[divider+1:]
    e_value_train = e_list[:divider]
    e_value_test = e_list[divider+1:]
    # Define the RNN layer
    tf.compat.v1.nn.dynamic_rnn
    rnn_cell = tf.compat.v1.nn.rnn_cell.LSTMCell(num_units=64)
    rnn_output, rnn_state = tf.compat.v1.nn.dynamic_rnn(rnn_cell, tf.concat([weight,z_value,e_value], axis=1), dtype=tf.float32)

    # Define the output layer
    output = tf.layers.dense(rnn_output[:, -1, :], units=1, activation=None)

    # Define the loss function and optimizer
    target = tf.placeholder(tf.float32, shape=[None, 1], name='target')
    loss = tf.losses.mean_squared_error(target, output)
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

    # Initialize the variables and start the session
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    # Train the model
    for i in range(3):
        _, loss_val = sess.run([optimizer, loss], feed_dict={weight: weight_train, z_value: z_value_train, e_value: e_value_train})
        
    # Evaluate the model
    demands_updated, graph_updated = sess.run(output, feed_dict={weight: weight_test, z_value: z_value_test, e_value: e_value_test})

    return demands_updated, graph_updated
