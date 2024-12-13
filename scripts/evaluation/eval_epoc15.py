# Congelar las capas iniciales del modelo
for param in model.parameters():
    param.requires_grad = False

# Descongelar solo las capas finales (última capa totalmente conectada y capas específicas de la arquitectura ResNet)
for param in model.layer4.parameters():
    param.requires_grad = True
for param in model.fc.parameters():
    param.requires_grad = True

    # Usar una tasa de aprendizaje (lr) más baja para el fine-tuning
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=1e-4)


# Re-entrenar el modelo con fine-tuning con epoch=15
num_epochs = 15
criterion = nn.CrossEntropyLoss()

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward pass y optimización
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}")

print("Fine-tuning completado.")


# Evaluación en el conjunto de prueba después de fine-tuning
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f'Precisión en el conjunto de prueba después de fine-tuning: {accuracy:.2f}%')