const algorithmSelect =
    document.getElementById("algorithm");

const operationContainer =
    document.getElementById("operation-container");

const operationSelect =
    document.getElementById("operation");

const form =
    document.getElementById("crypto-form");

const inputFields =
    document.getElementById("input-fields");

const submitButton =
    document.getElementById("submit-button");

const resultPanel =
    document.getElementById("result-panel");

const resultContent =
    document.getElementById("result-content");

const errorBox =
    document.getElementById("error-box");


// =====================================================
// Algorithm Configuration
// =====================================================

const algorithms = {

    // -------------------------------------------------
    // Substitution
    // -------------------------------------------------

    substitution: {

        operations: [],

        buttonText: "Run Substitution",

        fields: [
            {
                name: "plaintext",
                label: "Plaintext",
                type: "textarea",
                placeholder: "Enter plaintext..."
            },
            {
                name: "substitution_key",
                label: "26-Letter Permutation Key",
                type: "text",
                placeholder: "QWERTYUIOPASDFGHJKLZXCVBNM"
            }
        ]
    },


    // -------------------------------------------------
    // Double Transposition
    // -------------------------------------------------

    double_transposition: {

        operations: [
            {
                value: "encrypt",
                label: "Encrypt"
            },
            {
                value: "decrypt",
                label: "Decrypt"
            }
        ],

        fields: {

            encrypt: [
                {
                    name: "plaintext",
                    label: "Plaintext",
                    type: "textarea",
                    placeholder: "Enter plaintext..."
                },
                {
                    name: "row",
                    label: "Rows",
                    type: "number",
                    placeholder: "Suggested automatically"
                },
                {
                    name: "col",
                    label: "Columns",
                    type: "number",
                    placeholder: "Suggested automatically"
                },
                {
                    name: "row_key",
                    label: "Row Permutation Key",
                    type: "text",
                    placeholder: "Example: 2 0 1"
                },
                {
                    name: "column_key",
                    label: "Column Permutation Key",
                    type: "text",
                    placeholder: "Example: 1 3 0 2"
                }
            ],

            decrypt: [
                {
                    name: "ciphertext",
                    label: "Ciphertext",
                    type: "textarea",
                    placeholder: "Enter ciphertext..."
                },
                {
                    name: "row",
                    label: "Rows",
                    type: "number"
                },
                {
                    name: "col",
                    label: "Columns",
                    type: "number"
                },
                {
                    name: "row_key",
                    label: "Row Permutation Key",
                    type: "text",
                    placeholder: "Example: 2 0 1"
                },
                {
                    name: "column_key",
                    label: "Column Permutation Key",
                    type: "text",
                    placeholder: "Example: 1 3 0 2"
                }
            ]
        }
    },

    // -------------------------------------------------
    // DES
    // -------------------------------------------------

    des: {

        operations: [
            {
                value: "encrypt",
                label: "Encrypt"
            },
            {
                value: "decrypt",
                label: "Decrypt"
            }
        ],

        fields: {

            encrypt: [
                {
                    name: "plaintext",
                    label: "Plaintext",
                    type: "textarea",
                    placeholder: "Enter plaintext..."
                }
            ],

            decrypt: [
                {
                    name: "ciphertext",
                    label: "Ciphertext (Binary)",
                    type: "textarea",
                    placeholder: "Enter DES ciphertext..."
                },
                {
                    name: "key",
                    label: "64-bit DES Key",
                    type: "textarea",
                    placeholder: "Enter DES key..."
                }
            ]
        }
    },


    // -------------------------------------------------
    // AES
    // -------------------------------------------------

    aes: {

        operations: [
            {
                value: "encrypt",
                label: "Encrypt"
            },
            {
                value: "decrypt",
                label: "Decrypt"
            }
        ],

        fields: {

            encrypt: [
                {
                    name: "plaintext",
                    label: "Plaintext",
                    type: "textarea",
                    placeholder: "Enter plaintext..."
                }
            ],

            decrypt: [
                {
                    name: "ciphertext",
                    label: "Ciphertext",
                    type: "textarea",
                    placeholder: "Enter AES ciphertext..."
                },
                {
                    name: "key",
                    label: "AES Key",
                    type: "textarea",
                    placeholder: "Enter AES key..."
                }
            ]
        }
    },


    // -------------------------------------------------
    // RSA
    // -------------------------------------------------

    rsa: {

        operations: [
            {
                value: "generate_keys",
                label: "Generate Keys"
            },
            {
                value: "encrypt",
                label: "Encrypt"
            },
            {
                value: "decrypt",
                label: "Decrypt"
            }
        ],

        fields: {

            generate_keys: [
                {
                    name: "key_size",
                    label: "Key Size",
                    type: "select",
                    options: [
                        {
                            value: "512",
                            label: "512 bits"
                        },
                        {
                            value: "1024",
                            label: "1024 bits"
                        }
                    ]
                }
            ],

            encrypt: [
                {
                    name: "plaintext",
                    label: "Plaintext",
                    type: "textarea",
                    placeholder: "Enter plaintext..."
                },
                {
                    name: "e",
                    label: "Public Exponent (e)",
                    type: "textarea",
                    placeholder: "Enter e..."
                },
                {
                    name: "n",
                    label: "Modulus (n)",
                    type: "textarea",
                    placeholder: "Enter n..."
                }
            ],

            decrypt: [
                {
                    name: "ciphertext",
                    label: "Ciphertext",
                    type: "textarea",
                    placeholder: "Enter ciphertext integer..."
                },
                {
                    name: "d",
                    label: "Private Exponent (d)",
                    type: "textarea",
                    placeholder: "Enter d..."
                },
                {
                    name: "n",
                    label: "Modulus (n)",
                    type: "textarea",
                    placeholder: "Enter n..."
                }
            ]
        }
    },


    // -------------------------------------------------
    // ECC
    // -------------------------------------------------

    ecc: {

        operations: [
            {
                value: "generate",
                label: "Generate Points & Keys"
            },
            {
                value: "ecdh",
                label: "ECDH Key Exchange"
            }
        ],

        fields: {

            generate: [
                {
                    name: "p",
                    label: "Prime (p)",
                    type: "number"
                },
                {
                    name: "a",
                    label: "Curve Parameter (a)",
                    type: "number"
                },
                {
                    name: "b",
                    label: "Curve Parameter (b)",
                    type: "number"
                },
                {
                    name: "gx",
                    label: "Generator X (Gx)",
                    type: "number"
                },
                {
                    name: "gy",
                    label: "Generator Y (Gy)",
                    type: "number"
                },
                {
                    name: "n",
                    label: "Order (n)",
                    type: "number"
                }
            ],

            ecdh: [
                {
                    name: "p",
                    label: "Prime (p)",
                    type: "number"
                },
                {
                    name: "a",
                    label: "Curve Parameter (a)",
                    type: "number"
                },
                {
                    name: "b",
                    label: "Curve Parameter (b)",
                    type: "number"
                },
                {
                    name: "gx",
                    label: "Generator X (Gx)",
                    type: "number"
                },
                {
                    name: "gy",
                    label: "Generator Y (Gy)",
                    type: "number"
                },
                {
                    name: "n",
                    label: "Order (n)",
                    type: "number"
                },
                {
                    name: "alice_private",
                    label: "Alice Private Key",
                    type: "number"
                },
                {
                    name: "bob_private",
                    label: "Bob Private Key",
                    type: "number"
                }
            ]
        }
    }
};


algorithmSelect.addEventListener("change", () => {

    clearResult();

    const algorithm = algorithmSelect.value;

    inputFields.innerHTML = "";

    if (!algorithm) {
        operationContainer.classList.add("hidden");
        submitButton.classList.add("hidden");
        return;
    }

    const config = algorithms[algorithm];

    submitButton.classList.remove("hidden");


    if (config.operations.length > 0) {

        operationContainer.classList.remove("hidden");

        operationSelect.innerHTML = "";

        config.operations.forEach(operation => {

            const option =
                document.createElement("option");

            option.value = operation.value;
            option.textContent = operation.label;

            operationSelect.appendChild(option);
        });

    } else {

        operationContainer.classList.add("hidden");
        operationSelect.innerHTML = "";
    }

    renderFields();
});


operationSelect.addEventListener(
    "change",
    renderFields
);


function renderFields() {

    inputFields.innerHTML = "";

    const algorithm =
        algorithmSelect.value;

    if (!algorithm) {
        return;
    }

    const config =
        algorithms[algorithm];

    let fields;


    if (Array.isArray(config.fields)) {

        fields = config.fields;

        submitButton.textContent =
            config.buttonText || "Run";

    } else {

        const operation =
            operationSelect.value;

        fields =
            config.fields[operation] || [];

        const operationLabel =
            operationSelect
                .selectedOptions[0]
                ?.textContent;

        submitButton.textContent =
            operationLabel || "Run";
    }


    fields.forEach(field => {

        const wrapper =
            document.createElement("div");

        wrapper.className = "field";

        const label =
            document.createElement("label");

        label.htmlFor = field.name;
        label.textContent = field.label;

        let input;

        if (field.type === "textarea") {

            input =
                document.createElement("textarea");

        } else if (field.type === "select") {

            input =
                document.createElement("select");

            field.options.forEach(item => {

                const option =
                    document.createElement("option");

                option.value = item.value;
                option.textContent = item.label;

                input.appendChild(option);
            });

        } else {

            input =
                document.createElement("input");

            input.type = field.type;
        }

        input.id = field.name;
        input.name = field.name;
        input.required = true;

        if (field.placeholder) {
            input.placeholder = field.placeholder;
        }

        wrapper.appendChild(label);
        wrapper.appendChild(input);

        inputFields.appendChild(wrapper);
    });


if (
    algorithm === "double_transposition" &&
    operationSelect.value === "encrypt"
) {
    setupTranspositionSuggestions();
}
}


form.addEventListener("submit", async event => {

    event.preventDefault();

    clearResult();

    const algorithm =
        algorithmSelect.value;

    if (!algorithm) {
        showError(
            "Please select an algorithm."
        );
        return;
    }


    const payload = {
        algorithm: algorithm
    };


    const config =
        algorithms[algorithm];


    if (config.operations.length > 0) {

        payload.operation =
            operationSelect.value;
    }


    const formData =
        new FormData(form);


    for (const [key, value] of formData.entries()) {

        payload[key] = value;
    }


    submitButton.disabled = true;
    submitButton.textContent = "Processing...";


    try {

        const response = await fetch(
            "/api/crypto",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body:
                    JSON.stringify(payload)
            }
        );


        const data =
            await response.json();


        if (!data.success) {

            showError(
                data.error ||
                "Something went wrong."
            );

            return;
        }


        renderResult(
            algorithm,
            data.result
        );


    } catch (error) {

        showError(
            "Unable to communicate with the server."
        );

    } finally {

        submitButton.disabled = false;

        renderButtonText();
    }

});


function renderButtonText() {

    const algorithm =
        algorithmSelect.value;

    if (!algorithm) {
        return;
    }

    const config =
        algorithms[algorithm];


    if (config.operations.length === 0) {

        submitButton.textContent =
            config.buttonText || "Run";

        return;
    }


    submitButton.textContent =
        operationSelect
            .selectedOptions[0]
            ?.textContent || "Run";
}


function renderResult(algorithm, result) {

    resultPanel.classList.remove("hidden");

    switch (algorithm) {

        case "substitution":
            renderSubstitution(result);
            break;

        case "double_transposition":
            renderTransposition(result);
            break;

        case "des":
            renderSymmetric(
                result,
                "DES"
            );
            break;

        case "aes":
            renderSymmetric(
                result,
                "AES"
            );
            break;

        case "rsa":
            renderRSA(result);
            break;

        case "ecc":
            renderECC(result);
            break;
    }
}


// =====================================================
// Substitution Result
// =====================================================

function renderSubstitution(result) {

    let html = `
        <h2>Substitution Cipher Result</h2>

        ${output(
            "Plaintext",
            result.plaintext
        )}

        ${output(
            "Key",
            result.key
        )}

        ${output(
            "Ciphertext",
            result.ciphertext
        )}

        ${output(
            "Decrypted Text",
            result.decrypted
        )}
    `;

    html += frequencyTable(
        result.frequency
    );

    resultContent.innerHTML = html;
}


function renderTransposition(result) {

    let html =
        `<h2>Double Transposition Result</h2>`;


    if (result.operation === "encrypt") {

        html += output(
            "Plaintext",
            result.plaintext
        );

        html += output(
            "Matrix Size",
            `${result.row} × ${result.col}`
        );

        html += output(
            "Row Key",
            formatValue(result.row_key)
        );

        html += output(
            "Column Key",
            formatValue(result.column_key)
        );

        html += output(
            "Ciphertext",
            result.ciphertext
        );

        html += frequencyTable(
            result.frequency
        );

    } else {

        html += output(
            "Ciphertext",
            result.ciphertext
        );

        html += output(
            "Matrix Size",
            `${result.row} × ${result.col}`
        );

        html += output(
            "Decrypted Plaintext",
            result.plaintext
        );
    }


    resultContent.innerHTML = html;
}

function renderSymmetric(result, name) {

    let html =
        `<h2>${name} Result</h2>`;


    if (result.operation === "encrypt") {

        html += output(
            "Ciphertext",
            result.ciphertext
        );

        html += output(
            "Generated Key",
            result.key
        );


        if (result.decrypted !== undefined) {

            html += output(
                "Decrypted Text",
                result.decrypted
            );
        }


        if (result.round_keys) {

            html += `
                <h3>Round Keys</h3>

                <div class="round-keys">
            `;

            result.round_keys.forEach(
                (key, index) => {

                    html += `
                        <div class="round-key">
                            <span>
                                K${index + 1}
                            </span>

                            <code>
                                ${escapeHtml(
                                    formatValue(key)
                                )}
                            </code>
                        </div>
                    `;
                }
            );

            html += `</div>`;
        }

    } else {

        html += output(
            "Plaintext",
            result.plaintext
        );
    }


    resultContent.innerHTML = html;
}


function renderRSA(result) {

    let html = `<h2>RSA Result</h2>`;


    if (result.operation === "generate_keys") {

        html += `
            <h3>Public Key</h3>

            ${output(
                "e",
                result.public_key.e
            )}

            ${output(
                "n",
                result.public_key.n
            )}


            <h3>Private Key</h3>

            ${output(
                "d",
                result.private_key.d
            )}

            ${output(
                "n",
                result.private_key.n
            )}
        `;

    } else if (
        result.operation === "encrypt"
    ) {

        html += output(
            "Ciphertext",
            result.ciphertext
        );

    } else if (
        result.operation === "decrypt"
    ) {

        html += output(
            "Decrypted Plaintext",
            result.plaintext
        );
    }


    resultContent.innerHTML = html;
}


function renderECC(result) {

    let html = `<h2>ECC Result</h2>`;


    if (result.operation === "generate") {

        html += `
            <h3>Domain Parameters</h3>

            <div class="parameter-grid">

                ${smallOutput(
                    "p",
                    result.domain.p
                )}

                ${smallOutput(
                    "a",
                    result.domain.a
                )}

                ${smallOutput(
                    "b",
                    result.domain.b
                )}

                ${smallOutput(
                    "G",
                    formatPoint(
                        result.domain.G
                    )
                )}

                ${smallOutput(
                    "n",
                    result.domain.n
                )}

            </div>


            <h3>Generated Keys</h3>

            ${output(
                "Private Key",
                result.private_key
            )}

            ${output(
                "Public Key",
                formatPoint(
                    result.public_key
                )
            )}
        `;


        if (result.multiples) {

            html += `
                <h3>Multiples of G</h3>

                <div class="table-wrapper">

                    <table>

                        <thead>
                            <tr>
                                <th>Multiple</th>
                                <th>Point</th>
                            </tr>
                        </thead>

                        <tbody>
            `;


            result.multiples.forEach(
                item => {

                    html += `
                        <tr>
                            <td>
                                ${item[0]}G
                            </td>

                            <td>
                                ${escapeHtml(
                                    formatPoint(
                                        item[1]
                                    )
                                )}
                            </td>
                        </tr>
                    `;
                }
            );


            html += `
                        </tbody>
                    </table>

                </div>
            `;
        }

    } else if (
        result.operation === "ecdh"
    ) {

        html += `
            <div class="ecdh-grid">

                <div>
                    <h3>Alice</h3>

                    ${output(
                        "Private Key",
                        result.alice_private
                    )}

                    ${output(
                        "Public Key",
                        formatPoint(
                            result.alice_public
                        )
                    )}
                </div>


                <div>
                    <h3>Bob</h3>

                    ${output(
                        "Private Key",
                        result.bob_private
                    )}

                    ${output(
                        "Public Key",
                        formatPoint(
                            result.bob_public
                        )
                    )}
                </div>

            </div>


            <h3>Shared Key</h3>

            ${output(
                "ECDH Shared Key",
                formatPoint(
                    result.shared_key
                )
            )}
        `;
    }


    resultContent.innerHTML = html;
}

function frequencyTable(frequency) {

    if (!frequency || frequency.length === 0) {
        return "";
    }


    let rows = "";


    frequency.forEach(item => {

        rows += `
            <tr>
                <td>
                    ${escapeHtml(item.letter)}
                </td>

                <td>
                    ${item.count}
                </td>

                <td>
                    ${item.percentage}%
                </td>
            </tr>
        `;
    });


    return `
        <h3>Frequency Analysis</h3>

        <div class="table-wrapper">

            <table>

                <thead>
                    <tr>
                        <th>Letter</th>
                        <th>Count</th>
                        <th>Frequency</th>
                    </tr>
                </thead>

                <tbody>
                    ${rows}
                </tbody>

            </table>

        </div>
    `;
}

function output(label, value) {

    return `
        <div class="output-group">

            <label>
                ${escapeHtml(label)}
            </label>

            <div class="output-box">
                ${escapeHtml(
                    formatValue(value)
                )}
            </div>

        </div>
    `;
}


function smallOutput(label, value) {

    return `
        <div class="parameter">

            <span>${escapeHtml(label)}</span>

            <strong>
                ${escapeHtml(
                    formatValue(value)
                )}
            </strong>

        </div>
    `;
}


function formatValue(value) {

    if (value === null) {
        return "∞";
    }

    if (Array.isArray(value)) {
        return value.join(" ");
    }

    if (
        typeof value === "object"
    ) {
        return JSON.stringify(value);
    }

    return String(value);
}


function formatPoint(point) {

    if (point === null) {
        return "∞";
    }

    if (
        !Array.isArray(point) ||
        point.length !== 2
    ) {
        return formatValue(point);
    }

    return `(${point[0]}, ${point[1]})`;
}


function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


function showError(message) {

    errorBox.textContent = message;
    errorBox.classList.remove("hidden");
}


function clearResult() {

    errorBox.classList.add("hidden");
    errorBox.textContent = "";

    resultPanel.classList.add("hidden");
    resultContent.innerHTML = "";
}

function setupTranspositionSuggestions() {

    const plaintext =
        document.getElementById("plaintext");

    const rowInput =
        document.getElementById("row");

    const colInput =
        document.getElementById("col");

    const rowKey =
        document.getElementById("row_key");

    const colKey =
        document.getElementById("column_key");


    let rowManuallyChanged = false;
    let colManuallyChanged = false;


    rowInput.addEventListener("input", () => {
        rowManuallyChanged = true;

        updatePermutationSuggestions(
            rowInput,
            colInput,
            rowKey,
            colKey
        );
    });


    colInput.addEventListener("input", () => {
        colManuallyChanged = true;

        updatePermutationSuggestions(
            rowInput,
            colInput,
            rowKey,
            colKey
        );
    });


    plaintext.addEventListener("input", () => {

        const length =
            plaintext.value.length;

        if (length === 0) {
            return;
        }

        const suggested =
            suggestMatrixDimensions(length);


        if (!rowManuallyChanged) {
            rowInput.value =
                suggested.row;
        }

        if (!colManuallyChanged) {
            colInput.value =
                suggested.col;
        }


        updatePermutationSuggestions(
            rowInput,
            colInput,
            rowKey,
            colKey
        );
    });
}

function suggestMatrixDimensions(length) {

    let row =
        Math.floor(
            Math.sqrt(length)
        );

    if (row < 1) {
        row = 1;
    }

    const col =
        Math.ceil(
            length / row
        );

    return {
        row: row,
        col: col
    };
}

function updatePermutationSuggestions(
    rowInput,
    colInput,
    rowKey,
    colKey
) {

    const row =
        parseInt(rowInput.value);

    const col =
        parseInt(colInput.value);


    if (row > 0) {

        rowKey.placeholder =
            "Example: " +
            createIdentityPermutation(row);

    }


    if (col > 0) {

        colKey.placeholder =
            "Example: " +
            createIdentityPermutation(col);

    }
}


function createIdentityPermutation(size) {

    return Array
        .from(
            { length: size },
            (_, i) => i
        )
        .join(" ");
}